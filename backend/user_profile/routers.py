from rest_framework import routers

from user_profile.views import UserProfileViewSet

user_profile_router  = routers.DefaultRouter()
user_profile_router.register('', UserProfileViewSet)