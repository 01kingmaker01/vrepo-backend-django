from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'