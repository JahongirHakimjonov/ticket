# Generated by Django 5.0.8 on 2024-10-08 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0008_seattype_alter_ticket_options_ticket_seat_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="seattype",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Nomi"),
        ),
        migrations.AddField(
            model_name="seattype",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Nomi"),
        ),
    ]
