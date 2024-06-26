# Generated by Django 5.0.4 on 2024-04-29 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=299)),
                ('region', models.CharField(max_length=123)),
                ('post_code', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='media/villa')),
                ('area', models.CharField(max_length=17)),
                ('floor', models.PositiveSmallIntegerField()),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('bathroom', models.PositiveSmallIntegerField()),
                ('parking_lot', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('is_security', models.BooleanField(default=False)),
                ('authorization_type', models.PositiveSmallIntegerField(choices=[(1, 'Красная книга'), (2, 'Зеленая книга'), (3, 'Белая книга'), (4, 'Для аренды')])),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paymentmethod')),
            ],
        ),
    ]
