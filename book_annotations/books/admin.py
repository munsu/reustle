from django.contrib import admin
from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    pass

# Register your models here.
