from .models import Task, TaskProgress
from rest_framework import serializers
from django.apps import apps
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from users.serializers import UserSimpleSerializer
from reports.serializers import ReportSerailizer


class TaskProgressCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = TaskProgress
        fields = ['id', 'task', 'ordered_by',
                  'ordered_to', 'status', 'created_at']


class TaskProgressSerailizer(serializers.ModelSerializer):
    ordered_by = UserSimpleSerializer(many=False, read_only=True)
    ordered_to = UserSimpleSerializer(many=False, read_only=True)
    report = ReportSerailizer(many=True, read_only=True)

    class Meta:
        model = TaskProgress
        fields = ['url', 'id', 'task', 'ordered_by',
                  'ordered_to', 'status', 'report', 'created_at']


class TaskSerailizer(serializers.ModelSerializer):
    progresses = TaskProgressSerailizer(many=True, read_only=True)
    # owner = serializers.ReadOnlyField(source='users.name')

    class Meta:
        model = Task
        fields = ['url', 'id', 'task_name', 'secret', 'description', 'owner',
                  'priority', 'start_date', 'end_date', 'progresses']


class TaskTaskProgressSerailizer(NestedHyperlinkedModelSerializer):
    task = TaskSerailizer(many=False)

    class Meta:
        model = TaskProgress
        fields = ['url', 'id', 'task', 'ordered_by',
                  'ordered_to', 'status', 'created_at']


class TaskWithoutProgressSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'id', 'task_name', 'secret', 'description', 'owner',
                  'priority', 'start_date', 'end_date']


class TaskProgressUserSerailizer(serializers.HyperlinkedModelSerializer):
    task = TaskWithoutProgressSerailizer(many=False, read_only=True)

    ordered_by = UserSimpleSerializer(many=False, read_only=True)
    ordered_to = UserSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = TaskProgress
        fields = ['url', 'id', 'task', 'ordered_by',
                  'ordered_to', 'status', 'created_at']
