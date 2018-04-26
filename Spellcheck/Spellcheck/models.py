from django.db import models
from django.contrib.auth.models import User

#from datetime import datetime
#class User(models.Model):
#    email=models.EmailField()
#    name=models.CharField(max_length=100)
#    password=models.CharField(max_length=50)

#    def __str__(self):
  #      return self.name

class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key=models.CharField(max_length=128)
    language = models.CharField(max_length=50)
    textInputed=models.CharField(max_length=500)
    textChecked = models.CharField(max_length=500)
    textSuggestion=models.CharField(max_length=500)
    dateTimeCreated=models.DateTimeField(auto_now_add=True)
    dateTimeDelete = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.textInputed


