from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email']

        read_only_fields = ("username", "email")

        extra_kwargs = {
            "password": {'write_only': True}
        }


class UserRegistrationSerializer(UserSerializer):

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        refresh = RefreshToken.for_user(obj)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return tokens

    class Meta(UserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email', 'tokens']
        read_only_fields = ("tokens",)

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        exclude = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        address = Address.objects.create(user=user, **validated_data)
        return address


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)
