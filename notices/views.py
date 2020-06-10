from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import NoticeSerializer
from .models import Notice


# Create your views here.
class NoticeListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


# View to Update view count
class NoticeUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
