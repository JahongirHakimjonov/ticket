from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.ticket.filters import ConcertFilter
from apps.ticket.models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "user",
        "full_name",
        "total_price",
        "created_at",
        "is_paid",
    )
    search_fields = ("user__username", "user__phone", "user__telegram_id")
    list_filter = ("is_paid", "is_confirmed", ConcertFilter)
    actions = ["make_active", "make_inactive"]
    list_horizontal_scrollbar_top = True
    filter_horizontal = ("seat_numbers",)
    date_hierarchy = "created_at"
    list_filter_submit = True

    def make_active(self, request, queryset):  # noqa
        queryset.update(is_active=True)

    make_active.short_description = "Faol qilish"

    def make_inactive(self, request, queryset):  # noqa
        queryset.update(is_active=False)

    make_inactive.short_description = "Faol emas qilish"
