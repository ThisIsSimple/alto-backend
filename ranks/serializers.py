from .models import Rank
from rest_framework import serializers


class RankViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rank
        fields = ['id', 'url', 'name', 'rank_image', 'level']


class RankUpdateSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=30, required=False)

    class Meta:
        model = Rank
        fields = ['id', 'name', 'rank_image', 'level']


class RankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rank
        fields = ['id', 'name', 'rank_image', 'level']


class RankSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rank
        fields = ['name', 'rank_image']
