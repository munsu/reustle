from django.conf import settings
from django.db import models


class Book(models.Model):
    # from https://www.answers.com/Q/What_is_the_longest_book_title
    title = models.CharField(max_length=3999)
    number_of_pages = models.PositiveIntegerField()
    # - user can read all books, but update/delete only their own
    # ^ ownership of a book was a bit vague. I took the assumption that this
    # means owner is being the author of a book.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)


class Annotation(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    text = models.TextField()
    annotation_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
