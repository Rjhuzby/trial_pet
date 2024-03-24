# Generated by Django 5.0.2 on 2024-03-18 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=1)),
                ('stripe_payment_intent', models.CharField(blank=True, max_length=200, null=True)),
                ('has_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.product')),
            ],
        ),
    ]