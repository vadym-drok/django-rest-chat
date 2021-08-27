from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        fields = (
                'text',
                'owner_email',
                'created',
                'updated'
                )
        model = Message
