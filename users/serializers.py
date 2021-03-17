from .models import CustomUser
from rest_framework import serializers
from ranks.serializers import RankSerializer, RankSimpleSerializer
from ranks.models import Rank
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile_image = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'email', 'password', 'name', 'nickname', 'profile',
                  'profile_image', 'entered_at', 'birthday', 'phone', 'rank']


class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("create")
        print(validated_data)
        print(make_password(validated_data['password']))
        user = CustomUser.objects.create_user(
            username=validated_data.pop('username'),
            # password=make_password(
            #     validated_data.pop('password')
            # ),
            password=validated_data.pop('password'),
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        print("update")
        if 'user' in validated_data:
            instance.user.password = make_password(
                validated_data.get('user').get(
                    'password', instance.user.password)
            )
            instance.user.save()

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'email', 'password', 'name', 'nickname', 'profile',
                  'profile_image', 'entered_at', 'birthday', 'phone', 'rank']


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    rank = RankSerializer(many=False, read_only=True)
    task = serializers.ReadOnlyField(source='tasks.task')
    profile_image = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'email', 'name', 'nickname', 'profile',
                  'profile_image', 'entered_at', 'birthday', 'phone', 'rank', 'task', 'created_at', 'updated_at']


class UserSimpleSerializer(serializers.HyperlinkedModelSerializer):
    rank = RankSimpleSerializer(many=False, read_only=True)
    profile_image = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'name',
                  'profile_image', 'phone', 'rank']
