from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
# TODO: from apis.permissions import IsAuthenticated

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    # TODO: permission_classes = [IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # TODO: permission_classes = [IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer