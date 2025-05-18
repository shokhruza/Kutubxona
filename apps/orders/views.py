from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer
from ..users.permissions import IsUser, IsOperator, IsAdmin, IsAdminOrOperator


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsUser()]
        elif self.action in ['update', 'partial_update']:
            return [IsOperator() | IsAdmin()]
        elif self.action in ['list', 'retrieve']:
            return [IsOperator() | IsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'user':
            return Order.objects.filter(user=user)
        return Order.objects.all()

    @action(detail=True, methods=['post'], permission_classes=[IsOperator])
    def accept(self, request, pk=None):
        order = self.get_object()
        order.status = "accepted"
        order.save()
        return Response({'status': 'Buyurtma qabul qilindi'}, status=status.HTTP_200_OK)