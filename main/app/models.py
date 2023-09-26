# api/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    # Add more user-related fields as needed

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    # Add more client-related fields as needed

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    # Add more project-related fields as needed
