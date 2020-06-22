from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Entry, User
from .serializers import EntrySerializer, UserSerializer

# Create your views here.
class EntryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()

class UserListCreate(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

