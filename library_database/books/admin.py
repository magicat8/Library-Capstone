from django.contrib import admin
from .models import Book, ISBNEntry, customerRequest

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'isbn')
    search_fields = ('title', 'author', 'isbn')

@admin.register(ISBNEntry)
class ISBNEntryAdmin(admin.ModelAdmin):
    list_display = ('isbn',)
    search_fields = ('isbn',)

@admin.register(customerRequest)
class customerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')