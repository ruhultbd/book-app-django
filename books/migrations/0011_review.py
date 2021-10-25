# Generated by Django 3.2.8 on 2021-10-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
