from django.db import models


class User(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.id, self.email, self.name