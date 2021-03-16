from .models import Attachment
from rest_framework import viewsets, permissions
from .serializers import AttachmentViewSerializer, AttachmentCreateSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return AttachmentCreateSerializer
        return AttachmentViewSerializer

    queryset = Attachment.objects.all()
    serializer_class = AttachmentViewSerializer


class TaskAttachmentViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return AttachmentCreateSerializer
        return AttachmentViewSerializer

    def get_queryset(self):
        return Attachment.objects.filter(parent_type="task", parent=self.kwargs['task_pk'])

    queryset = Attachment.objects.all()
    serializer_class = AttachmentViewSerializer
