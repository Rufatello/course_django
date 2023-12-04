from django.contrib import admin
from mailings.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('Email', 'first_name', 'last_name', 'surname')

