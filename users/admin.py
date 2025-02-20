from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_staff", "is_superuser")
    search_fields = ("email", "username")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Персональная информация",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "phone_number",
                    "country",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
