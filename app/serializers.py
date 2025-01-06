# from rest_framework import serializers
# from .models import User, Subject, Mark

# class MarkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mark
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     marks = MarkSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = '__all__'

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = '__all__'
from rest_framework import serializers
from .models import User, Subject, Mark


class MarkSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)  # Add subject name

    class Meta:
        model = Mark
        fields = ['id', 'marks', 'subject', 'subject_name', 'user']  # Include subject_name


class UserSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(many=True, read_only=True)  # Use the updated MarkSerializer

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'marks']  # Include all necessary fields


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
