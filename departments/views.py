from .models import Department
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DepartmentSerializer, DepartmentListSerializer
from users.serializers import UserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    director = UserSerializer(many=False)

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list' or self.action == 'retrieve':
            return DepartmentListSerializer
        return DepartmentSerializer

    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
