from django.db import models

# Create your models here.
from django.db import models
class Computer(models.Model):
    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=16)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    computers = models.ForeignKey(Computer)

from datetime import datetime
class Book(models.Model):
    isbn = models.SlugField(max_length=20)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    published = models.DateTimeField(default=datetime.now)

