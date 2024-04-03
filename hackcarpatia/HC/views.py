from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

register_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="User name"),
        "password": openapi.Schema(
            type=openapi.TYPE_STRING, description="User password"
        ),
    },
    required=["username", "password"],
)


class RegisterView(APIView):
    @swagger_auto_schema(request_body=register_schema)
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                {"error": "Wymagane jest podanie nazwy użytkownika i hasła"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Użytkownik o tej nazwie już istnieje"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response(
            {"success": "Użytkownik został pomyślne zarejestrowany"},
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    @swagger_auto_schema(request_body=register_schema)
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(
                {"success": "Logowanie pomyślne"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Błędna nazwa użytkownika lub hasło"},
                status=status.HTTP_400_BAD_REQUEST,
            )

#shema for coordinates
coordinates_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "coordinates": openapi.Schema(type=openapi.TYPE_STRING, description="Coordinates")
    },
    required=["coordinates"],
)

class CoordinatesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('coordinates', openapi.IN_QUERY, description="Coordinates", type=openapi.TYPE_STRING)])
    def get(self, request):
        data = {"coordinates": "tutaj będą współrzędne"}
        return Response(data)
