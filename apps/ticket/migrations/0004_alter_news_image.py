# Generated by Django 5.0.8 on 2024-10-02 08:51

import apps.ticket.models.news
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(
                default=1,
                upload_to="news/",
                validators=[apps.ticket.models.news.validate_image_size],
                verbose_name="Rasm",
            ),
            preserve_default=False,
        ),
    ]
