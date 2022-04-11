
from .serializer import TodoListSerializer, UserDetailSerializer, TodoListDataValidationSerializer, TaskSerializer, TaskDataValidationSerializer
from .models import UserDetail, TodoList, SingleTodoList
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import exceptions

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

class UserDetailView(APIView):

    def post(self, request, format=None):
        try:
            if (User.objects.get(email=request.data.get("email"))):
                userObject = User.objects.get(email=request.data.get("email"))
                if (userObject.email == request.data.get("email")):
                    return Response({"error": "Email already registered with another Provider."})
        except User.DoesNotExist:
            print("user does not exists")

        user = User.objects.create_user(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        role = request.data.get("role")
        userDetail = UserDetailSerializer(data={"user": user.id})
        if userDetail.is_valid():
            userDetail.save()
            return Response({"status": "User Created", "details": userDetail.data})
        return Response({"error": "registeration failed."})

class TodoListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # throttle_classes = [UserRateThrottle]

    def Check_User_Auth(self, id):

        if id == self.request.user.id:
            return True
        else:
            raise exceptions.AuthenticationFailed

    def get(self, request, id=None):
        if id and self.Check_User_Auth(id):
            try:
                queryset = TodoList.objects.filter(user_id=id)
            except TodoList.DoesNotExist:
                return Response({'errors': 'This Transaction does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            read_TransactionSerializer = TodoListSerializer(queryset, many=True)

        return Response(read_TransactionSerializer.data)

    def post(self, request):

        validated_request = TodoListDataValidationSerializer(data=request.data)

        if validated_request.is_valid() and self.Check_User_Auth(validated_request.data.get('user_id')):
            validated_data = validated_request.data

            create_TodoSerializer = TodoListSerializer(data=validated_data)
            if create_TodoSerializer.is_valid():
                Todo_object = create_TodoSerializer.save()
                read_TodoSerializer = TodoListSerializer(Todo_object)
                return Response({"Todo": read_TodoSerializer.data, "status": "Todo Added successfully"},
                                status=status.HTTP_201_CREATED)
            # return False, create_TodoSerializer.errors
            return Response(data=create_TodoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(data={"status": "Logout Successful"}, status=status.HTTP_200_OK)

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
    try:
        tasks = SingleTodoList.objects.get(pk=pk)
        serializer = TaskSerializer(tasks, many=False)
        # return Response(serializer.data)
        return Response({"Task": serializer.data}, status=status.HTTP_200_OK)
    except SingleTodoList.DoesNotExist:
        return Response({'errors': 'This Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)


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
    try:
        task = SingleTodoList.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            task_object = TaskSerializer(task)
            return Response({"Task": task_object.data, "status": "Task Updated successfully"},
                            status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except SingleTodoList.DoesNotExist:
        return Response({'errors': 'This Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)



# api for overwriting a task completely
@api_view(['PUT'])
def UpdateTask(request, pk):
    try:
        task = SingleTodoList.objects.get(pk=pk)
        serializer = TaskSerializer(instance=task, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()
            task_object = TaskSerializer(task)
            return Response({"Task": task_object.data, "status": "Task Updated successfully"},
                            status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except SingleTodoList.DoesNotExist:
        return Response({'errors': 'This Task does not exist'}, status=status.HTTP_400_BAD_REQUEST)


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