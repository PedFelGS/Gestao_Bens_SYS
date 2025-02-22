from django.contrib import admin
from .models import Categories, Assets, Departments

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('figure','name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('figure','name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Assets)
class assetsAdmin(admin.ModelAdmin):
    list_display = ('figure','name', 'price', 'category', 'department','supplier', 'availability', 'created_at', 'updated_at')
    list_editable = ('price', 'availability')
    search_fields = ('name',)
    list_filter = ('category', 'availability')
    ordering = ('name',)
