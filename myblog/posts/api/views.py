from ast import Import
from requests import post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from yaml import serialize
from posts.models import Post
from posts.api.serializers import PostSerializer

# class PostApiView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         posts_serializer  = PostSerializer(posts, many=True)
#         return Response(status=status.HTTP_200_OK, data=posts_serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


class PostViewSet(ViewSet):
    def list(self, request):
        serializer  = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def create(self, request):
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)