from django.contrib import admin

# Register your models here.

from .models import Category, Auction

admin.site.register(Category)
admin.site.register(Auction)