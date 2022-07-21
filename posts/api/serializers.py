from configs.constant import USERS_URL

from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    ReadOnlyField
)

from posts.models import Post

import requests


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'userId', 'title', 'body']



class PostSerializerCreate(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        """Validation"""
        title = validated_data['title']
        body = validated_data['body']

        if Post.objects.filter(title=title).exists():
            raise ValidationError("Title is already exists")

        if Post.objects.filter(body=body).exists():
            raise ValidationError("Body is already exists")

        return Post.objects.create(**validated_data)

    def validate_userId(self, userId):
        """Validate by userId from external API"""
        users_response = requests.get(USERS_URL).json()

        if users_response == {}:
            raise ValidationError("External api is not valid")

        for user in users_response:
            if user['id'] == userId:
                return userId

        raise ValidationError("userId not found")


class PostSerializerUpdate(ModelSerializer):
    """Update only title and body"""
    userId = ReadOnlyField(source='userId.username')

    class Meta:
        model = Post
        fields = ['userId', 'title', 'body']

    def update(self, instance, validated_data):
        """Validation"""
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)

        if Post.objects.filter(title=validated_data['title']).exists():
            raise ValidationError("Title is already exists")

        if Post.objects.filter(body=validated_data['body']).exists():
            raise ValidationError("Body is already exists")

        instance.save()
        return instance
