from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from books.models import Book, Annotation


class BookList(LoginRequiredMixin, ListView):

    model = Book

    def get_queryset(self):
        """
        ?has_my_annotations=1 -> filter my annotated books
        ?has_my_annotations=0 -> filter my unannotated books
        """
        qs = super().get_queryset()
        if 'has_my_annotations' in self.request.GET:
            my_books = Annotation.objects.filter(
                annotation_author=self.request.user).values_list(
                    'book_id', flat=True)
            print(my_books)
            if self.request.GET['has_my_annotations'] == '1':
                qs = qs.filter(id__in=my_books)
            if self.request.GET['has_my_annotations'] == '0':
                qs = qs.filter(~Q(id__in=my_books))
        print(qs)
        return qs


class BookCreate(LoginRequiredMixin, CreateView):

    fields = ['title', 'number_of_pages', 'author']
    model = Book


class BookDetail(LoginRequiredMixin, DetailView):

    model = Book
    pk_url_kwarg = 'book_id'


class BookDelete(LoginRequiredMixin, DeleteView):
    """
    TODO permission checking
    """

    model = Book
    pk_url_kwarg = 'book_id'

    def get_success_url(self):
        return reverse('book-list')


class BookUpdate(LoginRequiredMixin, UpdateView):

    model = Book
    pk_url_kwarg = 'book_id'


class BookAnnotationList(LoginRequiredMixin, ListView):

    model = Annotation


class BookAnnotationCreate(LoginRequiredMixin, CreateView):
    """
    TODO validate page is less than book's number of pages
    """

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


class BookAnnotationDelete(LoginRequiredMixin, DeleteView):

    model = Annotation
    pk_url_kwarg = 'annotation_id'

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.book.pk})


class BookAnnotationUpdate(LoginRequiredMixin, UpdateView):
    """
    TODO validate page is less than book's number of pages
    """

    fields = ['page', 'text']
    model = Annotation
    pk_url_kwarg = 'annotation_id'

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.book.pk})
