from django.db import models

# Create your models here.

from django.db import models

class Items(models.Model):
    CATEGORY_CHOICES = [
        ('DRINKS', 'Drinks'),
        ('DESSERT', 'Dessert'),
        ('SNACKS', 'Snacks'),
        ('MAIN_MEAL', 'Main Meal'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/images', default='default.jpg')
    description = models.TextField()
    available = models.BooleanField(default=True)  # Use lowercase 'available' for field consistency
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='MAIN_MEAL')
   
    def __str__(self):
        return self.name  # This returns the name of the item when the object is printed

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['name']
