from rest_framework import serializers
from .models import User

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
