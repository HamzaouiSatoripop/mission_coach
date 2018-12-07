from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        return UserProfile.objects.filter(user = self.request.user)
    permission_classes = [IsAuthenticated]