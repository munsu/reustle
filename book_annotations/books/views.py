from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.views import ListView
from book_annotations.models import Book, Annotation


class BookList(ListView):

    model = Book


class BookCreate(CreateView):

    model = Book


class BookDetail(DetailView):

    model = Book


class BookDelete(DeleteView):

    model = Book


class BookUpdate(UpdateView):

    model = Book


class BookAnnotationList(ListView):

    model = Annotation


class BookAnnotationCreate(CreateView):

    model = Annotation


class BookAnnotationDelete(DeleteView):

    model = Annotation


class BookAnnotationUpdate(UpdateView):

    model = Annotation
