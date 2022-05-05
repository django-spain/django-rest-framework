from attr import field, fields
from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'order']
        # fields = '__all__'