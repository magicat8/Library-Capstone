from django.contrib import admin
from django.urls import path
from books.views import book_list, sales_report, unsold_books_report, index
from other.views import other_list
# Change the "View Site" link to point to the books path
admin.site.site_url = '/books/'

urlpatterns = [
    path('', index, name='index'),
    path('admin/books/sales_report/', sales_report, name='sales_report'),
    path('admin/books/unsold_books_report/', unsold_books_report, name='unsold_books_report'),
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),
    path('other products/', other_list, name='other_list')
]