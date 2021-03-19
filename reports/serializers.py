from .models import Report
from rest_framework import serializers
from django.apps import apps
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer


class ReportSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'task_progress', 'report_name',
                  'report_content', 'created_at', 'updated_at']


class ReportSimpleSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'report_name', 'report_content',
                  'created_at', 'updated_at']


class ReportCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'task_progress', 'report_name',
                  'report_content', 'created_at', 'updated_at']
