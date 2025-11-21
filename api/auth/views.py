from django.contrib.auth import authenticate
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.auth.serializers import LoginSerializer, ReadSerializer, RegistrationSerializer


class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({'detail': 'The user does not exist or incorrect password.'}, status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        user_serializer = ReadSerializer(user, context={'request':request})

        data = {
            **user_serializer.data,
            'token': token.key
        }

        return Response(data)


class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        user_serializer = ReadSerializer(user, context={'request':request})

        data = {
            **user_serializer.data,
            'token': token.key
        }

        return Response(data)

