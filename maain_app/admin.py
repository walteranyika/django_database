from django.contrib import admin

from maain_app.models import Customer

admin.site.site_title = "Nakuru Sacco Customers"
admin.site.site_header = "Sacco Application"

# how to customize django admin
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['names', 'email', 'gender']
    list_per_page = 20
    search_fields = ['names', 'email', 'dob', 'phone']
    list_filter = ['gender']



admin.site.register(Customer, CustomerAdmin)
