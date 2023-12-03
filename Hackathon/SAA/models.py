from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    sub = models.CharField(max_length=225)
    msg = models.TextField()

