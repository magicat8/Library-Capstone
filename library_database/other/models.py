from django.db import models

class Movie(models.Model):
    upc = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    copies = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title

class OtherProduct(models.Model):
    upc = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    copies = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.title} (Copies: {self.copies})"
    