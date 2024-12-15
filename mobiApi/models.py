from django.db import models

# Create your models here.
class Person (models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)


class User (models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    fullAcces = models.BooleanField(default=False)