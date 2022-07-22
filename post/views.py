from requests import post
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPagination
from rest_framework.generics import ListAPIView


class PostModelsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
