from .models import Rank
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RankViewSerializer, RankUpdateSerializer, RankSerializer


class RankViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RankViewSerializer
        if self.action == 'update' or self.action == 'update_partial':
            return RankUpdateSerializer
        return RankSerializer

    queryset = Rank.objects.all().order_by('-level')
    serializer_class = RankSerializer
    permission_classes = []
