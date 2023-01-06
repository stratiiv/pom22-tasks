from django.contrib import admin 
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def author(self, obj):
        return [i.name for i in obj.authors.all()]
    list_display = ['id', 'name', 'description', 'count', 'author']
    list_filter=('id','name','count')
    fieldsets=(
        ('Uneditable',{
            'fields':('name','year_of_publication',)
        }),
        ("Available",{
            'fields':('date_of_issue','description')
        }),
    )
admin.site.register(Book,BookAdmin)
