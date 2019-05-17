from django.conf import settings
from django.db import models
from django.urls import reverse


class Book(models.Model):
    # from https://www.answers.com/Q/What_is_the_longest_book_title
    title = models.CharField(max_length=3999)
    number_of_pages = models.PositiveIntegerField()
    # - user can read all books, but update/delete only their own
    # ^ I'm taking this to mean that a user can update/delete their own
    # annotations. Books can be deleted if no annotations are present.
    author = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.pk})

    def __str__(self):
        return f"{self.title} by {self.author}"


class Annotation(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, related_name="annotations")
    page = models.PositiveIntegerField()
    text = models.TextField()
    annotation_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    def __str__(self):
        return f"p.{self.page} on {self.book} annotated by {self.annotation_author}"