from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    upc = models.CharField(max_length=20, null=True, blank=True)
    copies = models.PositiveIntegerField(default=1)  # ← new field

    def __str__(self):
        return self.title

class OtherProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    upc = models.CharField(max_length=20, null=True, blank=True)
    copies = models.PositiveIntegerField(default=1)  # ← new field

    def __str__(self):
        return f"{self.title} (Copies: {self.copies})"
    