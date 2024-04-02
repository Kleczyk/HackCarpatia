from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Dodaj dodatkowe pola dla modelu użytkownika
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    # Możesz również dodać metody dla tego modelu
    def greet(self):
        return f"Hello, my name is {self.username} and I am {self.age} years old."
