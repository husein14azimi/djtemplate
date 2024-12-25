# account.serializers

from django.contrib.auth import get_user_model
from rest_framework import serializers
from jalali.serializers import JalaliDateTimeField

User = get_user_model()

class CombinedUserPersonSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='person.bio', allow_blank=True)
    birth_date = serializers.DateField(source='person.birth_date', allow_null=True)
    gender = serializers.CharField(source='person.gender', allow_null=True)
    updated_at = JalaliDateTimeField(source='person.updated_at', read_only=True)
    profile_picture = serializers.ImageField(source='person.profile_picture', allow_null=True)

    date_joined = JalaliDateTimeField(read_only=True)
    last_login = JalaliDateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'date_joined', 'last_login', 'bio', 'birth_date', 'gender', 'updated_at', 'profile_picture',]
        read_only_fields = ['id', 'username', 'date_joined', 'last_login',]