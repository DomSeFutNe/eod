from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, UserIsStaffViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# router.register(r'is_staff', UserIsStaffViewSet, basename='is_staff')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
user_routes = router