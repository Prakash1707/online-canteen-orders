from django.contrib import admin
from .models import details
from .models import foodItem
from .models import cart
from .models import transactions

admin.site.register(details)
admin.site.register(foodItem)
admin.site.register(cart)
admin.site.register(transactions)

# Register your models here.
