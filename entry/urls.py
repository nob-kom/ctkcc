from django.urls import path
from .views import EntryListCreateAPIView, UserListCreate, UserRetrieveUpdateDestroy

urlpatterns = [
    path('entries/', EntryListCreateAPIView.as_view()),
    path('users/', UserListCreate.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='detail'),
]
