from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from posts.models import Post

from .serializers import (
    PostSerializer,
    PostSerializerCreate,
    PostSerializerUpdate
)

from configs.constant import POSTS_URL

import requests


class PostList(APIView):
    """
    List all posts. Create a new post
    validate userID using external API.
    """

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializerCreate(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserIdPosts(APIView):
    """
    List of posts filtered by userId
    """

    def get(self, request, pk):
        post = Post.objects.filter(userId=pk)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    """
    Retrieve, update or delete a post. 
    If the post is not found in the database,
    it needs to be looked up using an external
    API and saved.
    """

    def get_object_or_create(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            posts_response = requests.get(POSTS_URL).json()

            if posts_response == {}:
                raise Http404

            for post in posts_response:
                if post['id'] == pk:
                    Post.objects.create(
                        id=post['id'],
                        userId=post['userId'],
                        title=post['title'],
                        body=post['body'],
                    )
                    return Post.objects.get(id=pk)

            raise Http404

    def get(self, request, pk):
        post = self.get_object_or_create(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializerUpdate(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
