from .models import Attachment
from users.serializers import UserSimpleSerializer
from rest_framework import serializers
from django.apps import apps
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from users.serializers import UserSimpleSerializer


class AttachmentViewSerializer(serializers.ModelSerializer):
    uploader = UserSimpleSerializer(many=False, read_only=True)
    attachment_file = serializers.ImageField()

    class Meta:
        model = Attachment
        fields = ['id', 'attachment_name', 'attachment_type',
                  'attachment_file', 'parent_type', 'parent', 'uploader', 'created_at', 'updated_at']


class AttachmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'attachment_name', 'attachment_type',
                  'attachment_file', 'parent_type', 'parent', 'uploader', 'created_at', 'updated_at']
