from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, mixins
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer
from .models import CustomUserModel


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserIsStaffViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View set to request if requested user is staff user.
    The api id is inside the path, defined as api_user_id.
    It returns a boolean.
    """
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        if self.get_queryset().first() is None:
            return Response(False)
        
        return Response(self.get_queryset().first().is_staff)
        
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]