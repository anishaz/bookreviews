from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User

# class ReviewManager(models.Manager):
#     def addReviewandBook(self,data):
#         user = User.objects.get(id=id)
#         self.create(rating=data['rating'], comment=data['comment'])

class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ReviewManager()

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(Book, related_name="book_reviews")
    user_id = models.ForeignKey(User, related_name="users")
    objects = ReviewManager()
