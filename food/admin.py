from django.contrib import admin
from food.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Food)
admin.site.register(Drink)
admin.site.register(Store)
admin.site.register(Order)
