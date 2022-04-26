from django.contrib import admin
from .models import Levels, Forms, Topping, Berries, Decors, OrderStatuses, Customers, Orders


admin.site.register(Customers)
admin.site.register(Levels)
admin.site.register(Forms)
admin.site.register(Topping)
admin.site.register(Berries)
admin.site.register(Decors)
admin.site.register(OrderStatuses)
admin.site.register(Orders)


