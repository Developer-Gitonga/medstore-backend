# Generated by Django 4.0.2 on 2022-06-29 11:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0002_rename_buyer_buying_buyer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buying',
            new_name='Purchasing',
        ),
    ]
