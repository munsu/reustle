from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('create/', views.BookCreate.as_view(), name='book-create'),
    path('<int:book_id>/', include([
        path('', views.BookDetail.as_view(), name='book-detail'),
        path('delete/', views.BookDelete.as_view(), name='book-delete'),
        path('update/', views.BookUpdate.as_view(), name='book-update'),
        path('annotations/', views.BookAnnotationList.as_view(), name='annotation-list'),
        path('annotations/create/', views.BookAnnotationCreate.as_view(), name='annotation-create'),
        path('annotations/<int:annotation_id>/', include([
            path('delete/', views.BookAnnotationDelete.as_view(), name='annotation-delete'),
            path('update/', views.BookAnnotationUpdate.as_view(), name='annotation-update'),
        ])),
    ])),
]
