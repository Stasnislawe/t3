import requests
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .models import SimpleModel


class SimpleModelSerializer(WritableNestedModelSerializer):
    user = serializers.CharField(max_length=100, read_only=True)

    # def _user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return request.user.username

    class Meta:
        model = SimpleModel
        fields = [
            'name',
            'iron_content',
            'si_content',
            'al_content',
            'ca_content',
            'sulfur_content',
            'create_time',
            'user',
        ]

        read_only_fields = ['user']

    def create(self, validated_data):
        model = SimpleModel.objects.create(**validated_data, user=self.context['request'].user)

        return model


