from django.contrib import admin
from .models import Cat, Feeding

# Register your models here.
if not admin.site.is_registered(Cat):
    admin.site.register(Cat)

if not admin.site.is_registered(Feeding):
    admin.site.register(Feeding)