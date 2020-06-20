from django.urls import path
from .views import EntryListCreateAPIView

urlpatterns = [
    path('entries/', EntryListCreateAPIView.as_view()),
]
