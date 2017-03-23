from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User

class ReviewManager(models.Manager):
    pass

class BookManager(models.Manager):
    pass

class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.CharField(max_length = 100)
    creator = models.ForeignKey(User, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="book_reviews")
    objects = ReviewManager()
