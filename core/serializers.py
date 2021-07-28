from rest_framework import serializers
from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'hacker_id', 'synced', 'time', 'type', 'hn_deleted', 'author', 'text', 'url', 'title', 'local']
        read_only_fields = ['hacker_id', 'synced', 'hn_deleted', 'local']
        extra_kwargs = {
            'type': {'required': False},
            'time': {'required': False},
            'author': {'required': False},
            'text': {'required': False},
            'url': {'required': False},
            'title': {'required': False},
        }

    def create(self, validated_data):
        obj = Base.objects.create(local=True, **validated_data)
        return obj
