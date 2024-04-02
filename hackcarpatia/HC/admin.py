from django.contrib import admin
from .models import CustomUser  # Załóżmy, że mamy model CustomUser
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin, User)

