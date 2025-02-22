from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "email", "admin", "created_at", "updated_at")
    list_filter = ("admin", "created_at")  
    search_fields = ("name", "email") 
    ordering = ("created_at",) 
    readonly_fields = ("created_at", "updated_at")  
    fieldsets = (
        ("Informações Pessoais", {
            "fields": ("name", "email", "password_hash"),
        }),
        ("Permissões e Status", {
            "fields": ("admin",),
        }),
        ("Datas Importantes", {
            "fields": ("created_at", "updated_at"),
        }),
    )