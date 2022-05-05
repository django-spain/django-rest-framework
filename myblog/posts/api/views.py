from ast import Import
from requests import post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from yaml import serialize
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class PostModeViewSet(ModelViewSet):
    # Si quiero que sea solo para usuarios autentificados.
    permission_classes = [IsAuthenticated]
    
    # Si esta autenticado puede leer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Com esto solo el usuario admin puede 
    # permission_classes = [IsAdminUser]
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

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


# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer  = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     def retrieve(self, request, pk: int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
    
#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)