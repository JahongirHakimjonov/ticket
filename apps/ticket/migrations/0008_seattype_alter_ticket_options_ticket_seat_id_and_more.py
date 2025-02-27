# Generated by Django 5.0.8 on 2024-10-08 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0007_alter_concert_map"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeatType",
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
            ],
            options={
                "verbose_name": "Joy turi",
                "verbose_name_plural": "Joy turlari",
                "db_table": "seat_type",
            },
        ),
        migrations.AlterModelOptions(
            name="ticket",
            options={"verbose_name": "Bilet", "verbose_name_plural": "Biletlar"},
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ticket.seat",
                verbose_name="Joy",
            ),
        ),
        migrations.AlterModelTable(
            name="ticket",
            table="ticket",
        ),
        migrations.CreateModel(
            name="SeatNumber",
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
                ("number", models.CharField(max_length=10)),
                (
                    "seat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seat_number",
                        to="ticket.seat",
                    ),
                ),
            ],
            options={
                "verbose_name": "O'rindiq raqami",
                "verbose_name_plural": "O'rindiq raqamlar",
                "db_table": "seat_number",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="seat_numbers",
            field=models.ManyToManyField(
                blank=True, to="ticket.seatnumber", verbose_name="O'rindiq raqamlari"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat_number",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ticket.seatnumber",
                verbose_name="O'rindiq raqami",
            ),
        ),
        migrations.AddField(
            model_name="seat",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ticket.seattype",
                verbose_name="Joy turi",
            ),
        ),
    ]
