from django.contrib import admin
from .models import ListOfServices, Order, Device, Client

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'service', 'creation_date', 'status', 'price']
    list_editable = ['status', 'price']

class ListOfServicesAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'device']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'username']

admin.site.register(Order, OrderAdmin)
admin.site.register(ListOfServices, ListOfServicesAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Client, ClientAdmin)