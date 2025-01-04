from rest_framework import serializers
from .models import User, Subject, Mark

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
