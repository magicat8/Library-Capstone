from django.contrib import admin
from django.urls import path
from books.views import book_list
from other.views import other_list
# Change the "View Site" link to point to the books path
admin.site.site_url = '/books/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),
    path('other products/', other_list, name='other_list')
]
