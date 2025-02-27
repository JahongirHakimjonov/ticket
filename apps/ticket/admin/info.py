from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.ticket.models import Info


@admin.register(Info)
class InfoAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at", "is_active")
    list_filter = ("created_at",)
    list_editable = ("is_active",)
    actions = ["make_active", "make_inactive"]
    list_filter_submit = True

    def make_active(self, request, queryset):  # noqa
        queryset.update(is_active=True)

    make_active.short_description = "Faol qilish"

    def make_inactive(self, request, queryset):  # noqa
        queryset.update(is_active=False)

    make_inactive.short_description = "Faol emas qilish"
