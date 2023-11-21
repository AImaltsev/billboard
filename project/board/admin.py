from django.contrib import admin
from .models import Category, Ad

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, CategoryAdmin)