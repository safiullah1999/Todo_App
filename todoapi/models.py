from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.utils.timezone import make_aware


# Create your models here.

class SingleTodoList(models.Model):
    C = "Completed"
    P = "Pending"
    CHOICES = (
        (C, "Completed"),
        (P, "Pending"),
    )
    task_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, choices=CHOICES, default="Pending")
    title = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=250, null=False, blank=False)

    class Meta:
        db_table = 'SingleTodoList'

