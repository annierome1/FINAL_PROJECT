#######################
#####
##### Admin Code that allows for models of editable exhbits and emal collection
#####
#######################

#imports needed functions
from django.contrib import admin
from .models import Exhibit, Email

#registers the exhibits and email models in admin
@admin.register(Exhibit)
class HTMLPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Email)
