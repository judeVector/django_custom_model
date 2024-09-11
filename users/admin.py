from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import NewUser


# Register your models here.
class UserAdminConfig(UserAdmin):

    list_filter = ["email", "user_name", "first_name", "is_active", "is_staff"]
    search_fields = ["email", "user_name", "first_name"]
    ordering = [
        "-start_date",
    ]
    list_display = ["email", "user_name", "first_name", "is_active", "is_staff"]
    fieldsets = [
        [
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                ),
            },
        ],
        ["Permissions", {"fields": ["is_staff", "is_active"]}],
        [
            "Personal",
            {
                "fields": [
                    "about",
                ]
            },
        ],
    ]


admin.site.register(NewUser, UserAdminConfig)
