from django.contrib import admin
from .models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    list_filter = ("email",)
    search_fields = ("id", "email")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "payment_amount")
    list_filter = ("date",)
    search_fields = (
        "date",
        "user",
    )
