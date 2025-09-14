from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class ModelAdmin (admin.ModelAdmin):
    list_display = ("username", "email", "role", "phone_number", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")

    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "phone_number")}),
    )

  
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "phone_number")}),
    )

    search_fields = ("username", "email", "role")
    ordering = ("username",)

admin.site.register(CustomUser, ModelAdmin)

