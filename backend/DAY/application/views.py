from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostListSerializer
from .models import Post
from rest_framework import permissions
from .permissions import IsOwner

class PostListAPIView(ListCreateAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes= (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostListSerializer
    permission_classes= (permissions.IsAuthenticated, IsOwner,)
    queryset = Post.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


