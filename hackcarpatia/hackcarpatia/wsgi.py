"""
WSGI config for hackcarpatia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackcarpatia.settings')


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # Tutaj powinieneś utworzyć token dla użytkownika i zwrócić go w odpowiedzi
            return Response({"message": "Zalogowano pomyślnie"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Nieprawidłowe dane logowania"}, status=status.HTTP_400_BAD_REQUEST)


application = get_wsgi_application()
