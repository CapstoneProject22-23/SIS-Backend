from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.IntegerField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    user_type = serializers.CharField(label=_("User Type"), write_only=True)
    # token = serializers.CharField(
    #     label=_("Token"),
    #     read_only=True
    # )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user_type = attrs.get('user_type')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password, user_type=user_type, backend='users.student_auth.backend.UserTypeAuthenticationBackend')

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
