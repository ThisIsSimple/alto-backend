from .models import CustomUser
from tasks.models import Task, TaskProgress
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, UserListSerializer, UserCreateSerializer
from tasks.serializers import TaskSerailizer, TaskProgressUserSerailizer


class UserViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            # permission_classes = [permissions.IsAuthenticated]
            return UserListSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []
    # permission_classes = [permissions.IsAuthenticated]


class UserTaskOwnViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Task.objects.filter(owner=self.kwargs['user_pk'])

    queryset = Task.objects
    serializer_class = TaskSerailizer


class UserTaskProgressViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return TaskProgress.objects.filter(ordered_to=self.kwargs['user_pk'])

    queryset = TaskProgress.objects
    serializer_class = TaskProgressUserSerailizer


class UserTaskProgressOrderedByViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return TaskProgress.objects.filter(ordered_by=self.kwargs['user_pk'])

    queryset = TaskProgress.objects
    serializer_class = TaskProgressUserSerailizer


class UserTaskProgressOrderedToViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return TaskProgress.objects.filter(ordered_to=self.kwargs['user_pk'])

    queryset = TaskProgress.objects
    serializer_class = TaskProgressUserSerailizer
