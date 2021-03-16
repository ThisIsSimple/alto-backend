from .models import Task, TaskProgress
from rest_framework import viewsets, permissions
from .serializers import TaskSerailizer, TaskTaskProgressSerailizer, TaskProgressSerailizer, TaskProgressCreateSerailizer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerailizer
    # permission_classes = [permissions.IsAuthenticated]


class TaskProgressViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return TaskProgressCreateSerailizer
        return TaskProgressSerailizer

    queryset = TaskProgress.objects
    serializer_class = TaskProgressSerailizer


class TaskTaskProgressViewSet(viewsets.ModelViewSet):
    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return TaskTaskProgressSerailizer
    #     return TaskProgressSerailizer

    def get_queryset(self):
        return TaskProgress.objects.filter(task=self.kwargs['task_pk'])

    queryset = TaskProgress.objects
    serializer_class = TaskTaskProgressSerailizer
