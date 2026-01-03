from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FeedView, LikePostView, UnlikePostView, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='post-feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
