from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header ='BRAVEMPIRE  ADMIN'
admin.site.site_title ='BRAVEMPIRE PORTAL'
admin.site.index_title='WELCOME TO BRAVEMPIRE ADMIN PORTAL'


class ContactAdminSite(admin.ModelAdmin):
    model = Contacts    

    list_display =('name', 'email', 'subject')

    list_filter = ['email', 'subject']

    search_fields = ['name', 'email', 'subject']

    fieldsets =[
        ("Contacts Details",{"fields":['name', 'email', 'subject', "message"]}),   

    ] 

admin.site.register(Contacts, ContactAdminSite)


