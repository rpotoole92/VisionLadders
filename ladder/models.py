from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class ProjectStatusLK(models.Model):
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class Project(models.Model):
  name = models.CharField(max_length=100)
  status = models.ForeignKey(ProjectStatusLK, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name

class TaskStatusLK(models.Model):
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Task(models.Model):
  name = models.CharField(max_length=100)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  parent_task = models.ForeignKey(
    'self', on_delete=models.CASCADE)
  status = models.ForeignKey(TaskStatusLK, on_delete=models.CASCADE)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
  assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to')
  assigned_date = models.DateTimeField()
  assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_by')
  scheduled_date = models.DateTimeField()
  due_date = models.DateTimeField()
  completed_date = models.DateTimeField()
  
  def __str__(self):
    return self.name