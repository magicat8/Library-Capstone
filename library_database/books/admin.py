from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
import requests

from .models import Book, ISBNEntry, customerRequest, Sale


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'condition', 'published_year', 'isbn', 'copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('condition', 'published_year')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity', 'sale_date')
    search_fields = ('book__title', 'book__author')
    list_filter = ('sale_date',)


@admin.register(ISBNEntry)
class ISBNEntryAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'condition')
    search_fields = ('isbn',)

    # Include custom JS file
    class Media:
        js = ("js/isbn_preview.js",)  # Put in books/static/js/

    # Add a custom URL for preview
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "preview-book/",
                self.admin_site.admin_view(self.preview_book),
                name="isbnentry-preview-book",
            ),
        ]
        return custom_urls + urls

    # Handle preview API call
    def preview_book(self, request):
        isbn = request.GET.get("isbn")
        condition = request.GET.get("condition")
        if not isbn:
            return JsonResponse({"error": "No ISBN provided"}, status=400)
        
        # First check if the book is already in inventory
        try:
            book = Book.objects.get(isbn=isbn)
            return JsonResponse(
                {
                    "title": book.title,
                    "author": book.author,
                    "published_year": book.published_year,
                    "publisher": book.publisher,
                    "description": book.description,
                    "page_count": book.page_count,
                    "language": book.language,
                    "categories": book.categories,
                    "price": str(book.price) if book.price is not None else None,
                    "copies": book.copies,
                    "in_inventory": True,
                }
            )
        except Book.DoesNotExist:
            pass  # Not in DB, try Google Books

        # If not in DB, fall back to Google Books API
        google_books_api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(google_books_api_url)

        if response.status_code == 200:
            data = response.json()
            if "items" in data and data["items"]:
                book_info = data["items"][0]["volumeInfo"]
                return JsonResponse(
                    {
                        "title": book_info.get("title"),
                        "author": ", ".join(book_info.get("authors", [])) if book_info.get("authors") else "Unknown",
                        "published_year": book_info.get("publishedDate"),
                        "publisher": book_info.get("publisher"),
                        "description": book_info.get("description"),
                        "page_count": book_info.get("pageCount"),
                        "language": book_info.get("language"),
                        "categories": ", ".join(book_info.get("categories", [])) if book_info.get("categories") else None,
                        "price": None,
                        "copies": None,
                        "in_inventory": False,
                    }
                )

        return JsonResponse({"error": "Book not found"}, status=404)


@admin.register(customerRequest)
class customerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
