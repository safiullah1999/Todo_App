
from .serializer import TaskSerializer, TaskDataValidationSerializer
from .models import SingleTodoList
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import exceptions

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
# Api without authentications

# api for getting all tasks
@api_view(['GET'])
def TaskList(request):
    tasks = SingleTodoList.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# api for getting info about single task
@api_view(['GET'])
def TaskInfo(request, pk):
    tasks = SingleTodoList.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


# api for creating a new task
@api_view(['POST'])
def CreateTask(request):
    validated_request = TaskDataValidationSerializer(data=request.data)
    if validated_request.is_valid():
        serializer = TaskSerializer(data=validated_request.data)

        if serializer.is_valid():
            task_object = serializer.save()
            task_object = TaskSerializer(task_object)
            return Response({"Task": task_object.data, "status": "Task Added successfully"},
                            status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=validated_request.errors, status=status.HTTP_400_BAD_REQUEST)


# api for updating a task
@api_view(['PATCH'])
def UpdateTaskStatus(request, pk):
    task = SingleTodoList.objects.get(pk=pk)
    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        task_object = TaskSerializer(task)
        return Response({"Task": task_object.data, "status": "Task Updated successfully"},
                        status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api for overwriting a task completely
@api_view(['PUT'])
def UpdateTask(request, pk):
    task = SingleTodoList.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data, partial=False)

    if serializer.is_valid():
        serializer.save()
        task_object = TaskSerializer(task)
        return Response({"Task": task_object.data, "status": "Task Updated successfully"},
                        status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# api to delete a task
@api_view(['DELETE'])
def DeleteTask(request, pk):
    try:
        task = SingleTodoList.objects.get(pk=pk)
        task_object = TaskSerializer(task)
        print(task_object.data)
        task.delete()
        return Response({"Task": task_object.data, "status": "Task Deleted successfully"},
                        status=status.HTTP_200_OK)
    except SingleTodoList.DoesNotExist:
        return Response({'errors': 'This Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)