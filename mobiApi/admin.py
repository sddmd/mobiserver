from django.contrib import admin
from .models import Person, User

admin.register(Person, User)


