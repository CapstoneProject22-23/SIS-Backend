from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'password',
                  'enrollment_number', 'date_of_birth']

        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    enrollment_number = serializers.IntegerField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        enrollment_number = attrs.get('enrollment_number')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            enrollment_number=enrollment_number,
            password=password
        )

        if not user:
            msg = ('Unable to authenticate')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


class AuthTokenSerializer(serializers.Serializer):
    enrollment_number = serializers.IntegerField(
        label=_("Enrollment Number"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    # token = serializers.CharField(
    #     label=_("Token"),
    #     read_only=True
    # )

    def validate(self, attrs):
        enrollment_number = attrs.get('enrollment_number')
        password = attrs.get('password')

        if enrollment_number and password:
            user = authenticate(request=self.context.get('request'),
                                username=enrollment_number, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
