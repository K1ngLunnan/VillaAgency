# Generated by Django 5.0.4 on 2024-04-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_bedrooms_house_bedroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
