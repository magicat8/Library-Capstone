from django.contrib import admin
from .models import OtherProduct, Movie

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'upc', 'copies')
    search_fields = ('title', 'upc')

@admin.register(OtherProduct)
class OtherProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'upc', 'copies')
    search_fields = ('title', 'upc')