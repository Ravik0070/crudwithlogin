from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=270)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title