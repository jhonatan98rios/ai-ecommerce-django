from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.name