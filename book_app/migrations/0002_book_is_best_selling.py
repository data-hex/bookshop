# Generated by Django 4.1.2 on 2022-12-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
