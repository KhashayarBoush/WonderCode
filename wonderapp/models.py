from django.db import models
import uuid
from django.db import IntegrityError

class User(models.Model):
    Name = models.CharField(max_length = 300)
    Family = models.CharField(max_length = 300)
    Phone = models.IntegerField(blank = True, null=True)
    Email = models.EmailField(blank = True, null = True)
    Project = models.TextField(help_text='please write your projects about')

    def __str__(self):
        return  self.Name + "   |  " + self.Family
