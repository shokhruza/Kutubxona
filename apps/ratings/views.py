from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from .models import BookRating
from .serializers import BookRatingSerializer
from ..users.permissions import IsUser


class BookRatingViewSet(viewsets.ModelViewSet):
    queryset = BookRating.objects.all()
    serializer_class = BookRatingSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsUser()]
        return [IsAuthenticated()]
