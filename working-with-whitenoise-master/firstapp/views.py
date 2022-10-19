from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from.models import datetime



#ViewSets define the view behavior
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer