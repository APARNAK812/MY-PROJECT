# Generated by Django 4.1.1 on 2023-01-06 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_seller_seller_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='user_name',
            field=models.IntegerField(default=0),
        ),
    ]
