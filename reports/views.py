from .models import Report
from rest_framework import viewsets, permissions
from .serializers import ReportSerailizer, ReportCreateSerailizer


class ReportViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return ReportCreateSerailizer
        return ReportSerailizer

    queryset = Report.objects.all()
    serializer_class = ReportSerailizer


class TaskReportViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return ReportCreateSerailizer
        return ReportSerailizer

    def get_queryset(self):
        return Report.objects.filter(task=self.kwargs['task_pk'])

    queryset = Report.objects.all()
    serializer_class = ReportSerailizer
