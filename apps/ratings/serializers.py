from rest_framework import serializers

from apps.ratings.models import BookRating


class BookRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = '__all__'