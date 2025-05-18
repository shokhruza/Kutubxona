from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return super().get_permissions()
