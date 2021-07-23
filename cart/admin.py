from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ExtendedUser)
admin.site.register(PlacedOrder)
admin.site.register(UserOtp)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(DeliveryAddress)
