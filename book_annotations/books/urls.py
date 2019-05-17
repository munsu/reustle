from django.urls import include, path
from . import views


urlpatterns = [
    path('/', views.BookList),
    path('create/', views.BookCreate),
    path('<int:book_id>/', include([
        path('/', views.BookDetail),
        path('delete/', views.BookDelete),
        path('update/', views.BookUpdate),
        path('annotations/', views.BookAnnotationList),
        path('annotations/create/', views.BookAnnotationCreate),
        path('annotations/<int:annotation_id>/', include([
            path('delete/', views.BookAnnotationDelete),
            path('update/', views.BookAnnotationUpdate),
        ])),
    ])),
]
