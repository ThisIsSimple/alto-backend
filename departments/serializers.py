from .models import Department
from rest_framework import serializers, permissions
from users.serializers import UserSerializer, UserSimpleSerializer


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'url', 'name',
                  'department_image', 'description', 'director']


class DepartmentListSerializer(serializers.HyperlinkedModelSerializer):
    director = UserSimpleSerializer(many=False)

    class Meta:
        model = Department
        fields = ['id', 'url', 'name',
                  'department_image', 'description', 'director']
