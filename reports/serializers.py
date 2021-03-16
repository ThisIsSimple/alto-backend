from .models import Report
from rest_framework import serializers
from django.apps import apps
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from users.serializers import UserSimpleSerializer


class ReportSerailizer(serializers.ModelSerializer):
    report_writer = UserSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'task', 'report_name',
                  'report_content', 'report_writer', 'created_at']


class ReportCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'task', 'report_name',
                  'report_content', 'report_writer', 'created_at']
