from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'PostList': '/post-list/',
        'PostDetail': '/post-detail/<str:pk>/',
        'PostCreate': '/post-create/',
        'PostUpdate': '/post-update/<str:pk>/',
        'PostDelete': '/post-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def post_list(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Item Succsesfully Delete!')
