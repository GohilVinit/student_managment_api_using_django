from rest_framework import generics
from .models import User, Subject, Mark
from .serializers import UserSerializer, SubjectSerializer, MarkSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        if instance.marks.exists():
            raise serializers.ValidationError("Cannot delete a user with marks.")
        instance.delete()

class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
