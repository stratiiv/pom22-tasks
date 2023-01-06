from django.contrib import admin 
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','surname','date_of_birth','date_of_death')
    fields=[('name','surname','patronymic'),'books',('date_of_birth','date_of_death')]
    list_filter=('name','surname','patronymic')
admin.site.register(Author,AuthorAdmin)