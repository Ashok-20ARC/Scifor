from django.contrib import admin
from .models import Laptop,Order,CartItem,Brand

admin.site.register(Brand)
admin.site.register(Laptop)
admin.site.register(Order)
admin.site.register(CartItem)

