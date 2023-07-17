from django.contrib import admin
from mainpageHW.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'generation')
    list_display_links = ('brand', 'model')
    search_fields = ('brand', 'model')
    ordering = ('-id',)
admin.site.register(Car, CarAdmin)


