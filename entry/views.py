from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Entry
from .serializers import EntrySerializer

# Create your views here.
class EntryListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
