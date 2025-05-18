from django.db import models
from django.conf import settings

from ..books.models import Book


class BookRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)  # 0-5
    created_at = models.DateTimeField(auto_now_add=True)