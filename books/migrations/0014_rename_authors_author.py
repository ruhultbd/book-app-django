# Generated by Django 3.2.8 on 2021-10-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20211014_0926'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]