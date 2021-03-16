from .models import Label
from rest_framework import serializers
# from ranks.serializers import RankSerializer, RankSimpleSerializer
# from ranks.models import Rank


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ['url', 'name', 'color']


class LabelTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ['url', 'name', 'color']
