from rest_framework import serializers
from .models import UserDetail, TodoList, SingleTodoList


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleTodoList
        fields = "__all__"


class TodoListDataValidationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(max_value=50, min_value=0, required=True)
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")


class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")

class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")