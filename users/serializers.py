from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())],
                "required": True,
            },
        }
        read_only_fields = ["is_superuser"]

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)
