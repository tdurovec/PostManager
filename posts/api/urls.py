from django.urls import path

from .views import PostList, PostDetail, UserIdPosts

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('user/<int:pk>/', UserIdPosts.as_view()),
]
