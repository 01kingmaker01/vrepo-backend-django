from .serializers import *
from django.shortcuts import redirect, render
from . models import Post

#import rest framwork components
from rest_framework import serializers

from rest_framework.generics import ListCreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from . paginations import PostCursorPagination




# Create your views here.

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})           

class PostCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer
    pagination_class = PostCursorPagination


class PostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer
    lookup_field = 'id'
    pagination_class = PostCursorPagination

   

class PostUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer   
    lookup_field = 'id'       
    pagination_class = PostCursorPagination
