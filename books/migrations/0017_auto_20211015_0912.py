# Generated by Django 3.2.8 on 2021-10-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='thumnail',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='review'),
        ),
    ]
