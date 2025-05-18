from django.db import models

from ..users.models import User
from ..books.models import Book

class StatusChoices(models.TextChoices):
    ORDERED = 'ORDERED', "Ordered"
    RETURNED = 'RETURNED', "Returned"
    ACCEPTED = 'ACCEPTED', "Accepted"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices)
    penalty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

