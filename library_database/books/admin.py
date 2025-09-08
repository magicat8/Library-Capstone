from django.contrib import admin
from .models import Book, ISBNEntry

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'isbn')
    search_fields = ('title', 'author', 'isbn')

@admin.register(ISBNEntry)
class ISBNEntryAdmin(admin.ModelAdmin):
    list_display = ('isbn',)
    search_fields = ('isbn',)
