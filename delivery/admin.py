from django.contrib import admin

# Register your models here.

from .models import Category, DeliveryModel

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title','description','category','price','datetime')
    list_display_links = ('title','description')
    search_fields = ('title','datetime','description')


admin.site.register(DeliveryModel,DeliveryAdmin)
admin.site.register(Category)
