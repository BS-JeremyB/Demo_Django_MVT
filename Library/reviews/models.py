from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    note = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return f"{self.user} attribue la note de {self.note}/10 au livre : {self.book}"