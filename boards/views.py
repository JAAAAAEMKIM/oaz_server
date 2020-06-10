from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from boards.models import Post, Comment, LikeComment, LikePost
from boards.serializers import PostSerializer, CommentSerializer, \
    LikeCommentSerializer, LikePostSerializer
from apis.permissions import IsOwner
# TODO: from apis.permissions import IsAuthenticated

# Posts
class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        serializer.get(post, {'views':post.views})
        return Response(serializer.data)
        


class PostUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Comments
class CommentCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Likes
class LikePostView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer


class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer


class LikeCommentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer


class UnlikeCommentView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer
