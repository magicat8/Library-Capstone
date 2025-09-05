import isbnlib
import requests # For making API calls to external services

def get_book_metadata(isbn):
    # 1. Validate the ISBN using isbnlib
    if not isbnlib.is_isbn13(isbn) and not isbnlib.is_isbn10(isbn):
        print("Invalid ISBN.")
        return None

    # 2. Use Google Books API to get metadata
    google_books_api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(google_books_api_url)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data and data['items']:
            book_info = data['items'][0]['volumeInfo']
            
            # Extract multiple metadata fields if available
            metadata = {
                "title": book_info.get("title"),
                "authors": book_info.get("authors"),
                "publisher": book_info.get("publisher"),
                "publishedDate": book_info.get("publishedDate"),
                "description": book_info.get("description"),
                "pageCount": book_info.get("pageCount"),
                "language": book_info.get("language"),
                "categories": book_info.get("categories") 
                              or [book_info.get("mainCategory")] 
                              if book_info.get("mainCategory") else None
            }
            return metadata
    return None

# Example usage:
isbn_to_check = "9780743273565" # Example ISBN
metadata = get_book_metadata(isbn_to_check)

if metadata:
    print(f"Metadata for ISBN {isbn_to_check}:")
    for key, value in metadata.items():
        print(f"{key.capitalize()}: {value}")
else:
    print(f"Could not find metadata for ISBN {isbn_to_check}.")
