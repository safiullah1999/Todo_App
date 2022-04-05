from rest_framework import serializers
from .models import SingleTodoList



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleTodoList
        fields = "__all__"


class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")

class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")