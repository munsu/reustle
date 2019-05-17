from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from books.models import Book, Annotation


class BookList(ListView):

    model = Book


class BookCreate(CreateView):

    model = Book


class BookDetail(DetailView):

    model = Book
    pk_url_kwarg = 'book_id'


class BookDelete(DeleteView):

    model = Book
    pk_url_kwarg = 'book_id'

    def get_success_url(self):
        return reverse('book-list')


class BookUpdate(UpdateView):

    model = Book
    pk_url_kwarg = 'book_id'


class BookAnnotationList(ListView):

    model = Annotation


class BookAnnotationCreate(CreateView):

    fields = ['page', 'text']
    model = Annotation
    pk_url_kwarg = 'annotation_id'

    def form_valid(self, form):
        form.instance.annotation_author = self.request.user
        form.instance.book_id = self.kwargs['book_id']
        print(self.kwargs)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.kwargs['book_id']})


class BookAnnotationDelete(DeleteView):

    model = Annotation
    pk_url_kwarg = 'annotation_id'

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.book.pk})


class BookAnnotationUpdate(UpdateView):

    fields = ['page', 'text']
    model = Annotation
    pk_url_kwarg = 'annotation_id'

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.book.pk})
