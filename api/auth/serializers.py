from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from account.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(validators=[validate_password], max_length=128)
    password2 =serializers.CharField(max_length=128)
    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def validate(self, attrs):
        pas1 = attrs.get('password1')
        pas2 = attrs.get('password2')

        if pas2 != pas1:
            raise serializers.ValidationError({'password2': ['The passwords do not match']})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        validated_data['password'] = make_password(password)

        return super().create(validated_data)



class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'date_joined', 'password', 'user_permissions', 'is_active', 'is_staff', 'is_superuser')