from rest_framework import serializers
from .models import Order
from datetime import date

class OrderSerializer(serializers.ModelSerializer):
    penalty = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_penalty(self, obj):
        today = date.today()
        if obj.due_date and today > obj.due_date:
            overdue_days = (today - obj.due_date).days
            penalty = int(obj.book.daily_price * 0.01 * overdue_days)
            return penalty
        return 0