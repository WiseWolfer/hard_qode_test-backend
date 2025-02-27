from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    Who_use = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subscription
        fields = (
            'name_of_subscription',
            'Flag_subscripton',
            'Who_use'
        )
