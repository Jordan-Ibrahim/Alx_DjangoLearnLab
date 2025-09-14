
from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import CustomUserAdmin

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


class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'publication_year')
   search_fields = ('title', 'author')
   list_filter = ('author', 'publication_year')


admin.site.register(Book, BookAdmin, CustomUser, CustomUserAdmin)


