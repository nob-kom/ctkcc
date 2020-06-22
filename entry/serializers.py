from rest_framework import serializers
from .models import Entry, User

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'id',
            'title',
            'content',
            'date'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'tower',
            'room_number',
            'name',
            'email_1',
            'email_2',
            'tel_1',
            'tel_2',
            'admission_date',
            'secession_date',
            'note'
        )
