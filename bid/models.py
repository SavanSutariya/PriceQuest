from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return 'images/default.png'
class Auction(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='auctions/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Active')
    increment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='winner')
    winner_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    winner_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name    
    
    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return 'images/default.png'