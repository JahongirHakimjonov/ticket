from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import AbstractBaseModel


class Order(AbstractBaseModel):
    user = models.ForeignKey(
        "BotUsers", on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi")
    )
    concert = models.ForeignKey(
        "Concert", on_delete=models.CASCADE, verbose_name=_("Konsert")
    )
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE, verbose_name=_("Joy"))
    seat_numbers = models.ManyToManyField(
        "SeatNumber", verbose_name=_("O'rindiq raqamlari"), blank=True
    )
    count = models.PositiveIntegerField(default=0, verbose_name=_("Soni"))
    total_price = models.DecimalField(
        max_digits=100, decimal_places=2, default=0.00, verbose_name=_("Jami narx")
    )
    full_name = models.CharField(max_length=255, verbose_name=_("Ism va Familiya"))
    phone = models.CharField(max_length=20, verbose_name=_("Telefon raqam"))
    is_confirmed = models.BooleanField(default=False, verbose_name=_("Tasdiqlandi"))
    is_paid = models.BooleanField(default=False, verbose_name=_("To'landi"))

    def __str__(self):
        return f"Order for {self.user} - {self.concert.name}, Total: {self.total_price}"

    class Meta:
        db_table = "order"
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")
