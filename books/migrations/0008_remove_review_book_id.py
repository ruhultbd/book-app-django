# Generated by Django 3.2.8 on 2021-10-13 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_review_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_id',
        ),
    ]
