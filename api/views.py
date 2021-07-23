from .serializers import *
from django.shortcuts import render
from . models import Post

#import rest framwork components
from rest_framework import serializers

from rest_framework.generics import ListCreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from . paginations import PostCursorPagination




# Create your views here.
class PostCreate(ListCreateAPIView):
    # print(request.headers)
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer
    pagination_class = PostCursorPagination


class PostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer
    lookup_field = 'id'

   

class PostUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostsSerializer   
    lookup_field = 'id'       