from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Qna, QnaComment, LikeQna, LikeQnaComment
from .serializers import QnaSerializer, QnaCommentSerializer, \
    LikeQnaCommentSerializer, LikeQnaSerializer
from apis.permissions import IsOwner
# TODO: from apis.permissions import IsAuthenticated

# QnAs
class QnaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer


class QnaRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer

    def get(self, request, pk):
        qna = Qna.objects.get(id=pk)
        serializer = QnaSerializer(qna)
        serializer.get(qna, {'views':qna.views})
        return Response(serializer.data)


class QnaUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer


# Comments
class QnaCommentCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = QnaComment.objects.all()
    serializer_class = QnaCommentSerializer


class QnaCommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = QnaComment.objects.all()
    serializer_class = QnaCommentSerializer


# Likes
class LikeQnaView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LikeQna.objects.all()
    serializer_class = LikeQnaSerializer


class UnlikeQnaView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = LikeQna.objects.all()
    serializer_class = LikeQnaSerializer


class LikeCommentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LikeQnaComment.objects.all()
    serializer_class = LikeQnaCommentSerializer


class UnlikeCommentView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = LikeQnaComment.objects.all()
    serializer_class = LikeQnaCommentSerializer
