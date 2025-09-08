from django.db import models
import isbnlib
import requests

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.CharField(max_length=20, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    categories = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    copies = models.PositiveIntegerField(default=1)  # ← new field

    def __str__(self):
        return f"{self.title} by {self.author} (Copies: {self.copies})"


class ISBNEntry(models.Model):
    isbn = models.CharField(max_length=20, null=False, blank=True)

    def save(self, *args, **kwargs):
        import isbnlib, requests

        google_books_api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{self.isbn}"
        response = requests.get(google_books_api_url)

        if response.status_code == 200:
            data = response.json()
            if 'items' in data and data['items']:
                book_info = data['items'][0]['volumeInfo']

                # Check if the book already exists
                book, created = Book.objects.get_or_create(
                    isbn=self.isbn,
                    defaults={
                        "title": book_info.get("title"),
                        "author": ", ".join(book_info.get("authors", [])) if book_info.get("authors") else "Unknown",
                        "published_year": book_info.get("publishedDate"),
                        "publisher": book_info.get("publisher"),
                        "description": book_info.get("description"),
                        "page_count": book_info.get("pageCount"),
                        "language": book_info.get("language"),
                        "categories": ", ".join(book_info.get("categories", [])) if book_info.get("categories") else None,
                        "copies": 1,
                    }
                )

                if not created:
                    # Book already exists, increment copies
                    book.copies += 1
                    book.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.isbn
