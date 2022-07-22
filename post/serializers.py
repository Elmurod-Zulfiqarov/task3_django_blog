from rest_framework.serializers import ModelSerializer
from post.models import Post, Comment


class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

	
class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
		depth = 1
		