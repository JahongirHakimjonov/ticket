# Generated by Django 5.0.8 on 2024-09-27 13:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BotUsers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "telegram_id",
                    models.BigIntegerField(unique=True, verbose_name="Telegram ID"),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Foydalanuvchi nomi",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Ism"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Familiya"
                    ),
                ),
                (
                    "phone",
                    models.BigIntegerField(
                        blank=True, null=True, unique=True, verbose_name="Telefon raqam"
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        choices=[
                            ("uz", "O'zbek tili"),
                            ("ru", "Rus tili"),
                            ("en", "Ingliz tili"),
                        ],
                        max_length=10,
                        verbose_name="Til",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Faolmi")),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Admin"),
                            ("moderator", "Moderator"),
                            ("user", "Foydalanuvchi"),
                        ],
                        default="user",
                        max_length=10,
                        verbose_name="Rol",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bot Foydalanuvchisi",
                "verbose_name_plural": "Bot Foydalanuvchilari",
                "db_table": "bot_users",
            },
        ),
        migrations.CreateModel(
            name="Concert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Nomi"),
                ),
                (
                    "name_uz",
                    models.CharField(
                        max_length=255, null=True, unique=True, verbose_name="Nomi"
                    ),
                ),
                (
                    "name_ru",
                    models.CharField(
                        max_length=255, null=True, unique=True, verbose_name="Nomi"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Sarlavha")),
                (
                    "title_uz",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Sarlavha"
                    ),
                ),
                (
                    "title_ru",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Sarlavha"
                    ),
                ),
                ("description", models.TextField(verbose_name="Tavsif")),
                ("description_uz", models.TextField(null=True, verbose_name="Tavsif")),
                ("description_ru", models.TextField(null=True, verbose_name="Tavsif")),
                ("date", models.DateField(verbose_name="Sanasi")),
                ("time", models.TimeField(verbose_name="Vaqt")),
                (
                    "min_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=100, verbose_name="Eng arzon narx"
                    ),
                ),
                (
                    "max_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=100, verbose_name="Eng qimmat narx"
                    ),
                ),
                ("address", models.CharField(max_length=255, verbose_name="Manzil")),
                (
                    "address_uz",
                    models.CharField(max_length=255, null=True, verbose_name="Manzil"),
                ),
                (
                    "address_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Manzil"),
                ),
                (
                    "location_google_maps",
                    models.URLField(max_length=255, verbose_name="Google Maps manzili"),
                ),
                (
                    "location_yandex_maps",
                    models.URLField(max_length=255, verbose_name="Yandex Maps manzili"),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="concerts",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["jpg", "png"]
                            )
                        ],
                        verbose_name="Rasm",
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="concerts/thumbnail",
                        verbose_name="Mini rasm",
                    ),
                ),
            ],
            options={
                "verbose_name": "Konsert",
                "verbose_name_plural": "Konsertlar",
                "db_table": "concert",
            },
        ),
        migrations.CreateModel(
            name="Info",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Nomi"),
                ),
                (
                    "name_uz",
                    models.CharField(
                        max_length=255, null=True, unique=True, verbose_name="Nomi"
                    ),
                ),
                (
                    "name_ru",
                    models.CharField(
                        max_length=255, null=True, unique=True, verbose_name="Nomi"
                    ),
                ),
                ("description", models.TextField(verbose_name="Tavsif")),
                ("description_uz", models.TextField(null=True, verbose_name="Tavsif")),
                ("description_ru", models.TextField(null=True, verbose_name="Tavsif")),
                (
                    "phone",
                    models.CharField(max_length=255, verbose_name="Telefon raqam"),
                ),
                (
                    "username",
                    models.CharField(max_length=255, verbose_name="Telegram username"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("location", models.URLField(max_length=255, verbose_name="Lokatsiya")),
                ("address", models.CharField(max_length=255, verbose_name="Manzil")),
                (
                    "address_uz",
                    models.CharField(max_length=255, null=True, verbose_name="Manzil"),
                ),
                (
                    "address_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Manzil"),
                ),
            ],
            options={
                "verbose_name": "Ma'lumot",
                "verbose_name_plural": "Ma'lumotlar",
                "db_table": "info",
            },
        ),
        migrations.CreateModel(
            name="Donate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=100, verbose_name="Summa"
                    ),
                ),
                (
                    "is_paid",
                    models.BooleanField(default=False, verbose_name="To'landi"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticket.botusers",
                        verbose_name="Foydalanuvchi",
                    ),
                ),
            ],
            options={
                "verbose_name": "Xayriya",
                "verbose_name_plural": "Xayriyalar",
                "db_table": "donate",
            },
        ),
        migrations.CreateModel(
            name="Seat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nomi")),
                (
                    "name_uz",
                    models.CharField(max_length=255, null=True, verbose_name="Nomi"),
                ),
                (
                    "name_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Nomi"),
                ),
                ("count", models.PositiveIntegerField(verbose_name="Joylar soni")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=100, verbose_name="Narx"
                    ),
                ),
                (
                    "concert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ticket.concert"
                    ),
                ),
            ],
            options={
                "verbose_name": "Joy",
                "verbose_name_plural": "Joylar",
                "db_table": "seat",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                ("count", models.PositiveIntegerField(default=0, verbose_name="Soni")),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=100,
                        verbose_name="Jami narx",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="Ism va Familiya"),
                ),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Telefon raqam"),
                ),
                (
                    "is_confirmed",
                    models.BooleanField(default=False, verbose_name="Tasdiqlandi"),
                ),
                (
                    "is_paid",
                    models.BooleanField(default=False, verbose_name="To'landi"),
                ),
                (
                    "concert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticket.concert",
                        verbose_name="Konsert",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticket.botusers",
                        verbose_name="Foydalanuvchi",
                    ),
                ),
                (
                    "seat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ticket.seat",
                        verbose_name="Joy",
                    ),
                ),
            ],
            options={
                "verbose_name": "Buyurtma",
                "verbose_name_plural": "Buyurtmalar",
                "db_table": "order",
            },
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan vaqti"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan vaqti"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktivmi"),
                ),
                ("ticket_id", models.CharField(max_length=255, null=True)),
                (
                    "ticket_id_url",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                ("ticket", models.ImageField(upload_to="tickets/")),
                ("seat", models.CharField(max_length=255, null=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="ticket.order",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
