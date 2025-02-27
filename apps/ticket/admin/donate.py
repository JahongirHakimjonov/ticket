from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.ticket.models import Donate


@admin.register(Donate)
class DonateAdmin(ModelAdmin):
    list_display = ("id", "user", "amount", "created_at", "is_paid")
    search_fields = ("user__username", "user__phone", "user__telegram_id")
    list_filter = ("created_at", "is_paid")
    list_filter_submit = True
