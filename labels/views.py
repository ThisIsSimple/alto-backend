from .models import Label
from rest_framework import viewsets, permissions
from .serializers import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    # def get_serializer_class(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return UserListSerializer
    #     return UserSerializer

    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    # permission_classes = [permissions.IsAuthenticated]
