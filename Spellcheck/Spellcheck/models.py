from django.db import models


class User(models.Model):
    email=models.EmailField(default=None)
    name=models.CharField(max_length=100, default=None)
    password=models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Text(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    language = models.CharField(max_length=50, default=None)
    text=models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.text


