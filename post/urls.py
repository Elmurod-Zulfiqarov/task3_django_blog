from django.urls import path, include

from .views import PostModelsViewSet, CommentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", PostModelsViewSet, basename="posts")

urlpatterns = [
	path('', include(router.urls)),
	path('comment', CommentListView.as_view(), name="comment")
]
