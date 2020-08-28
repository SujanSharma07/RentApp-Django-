

# Register your models here.

from django.contrib import admin
from main.models import Customers_model,RentRecords



@admin.register(Customers_model,RentRecords)
class AppAdmin(admin.ModelAdmin):
    pass
# Register your models here.
