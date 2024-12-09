# Generated by Django 5.1.4 on 2024-12-09 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.product')),
                ('tiered_discounts', models.JSONField(default=dict)),
            ],
            bases=('pricing.product',),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PremiumProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.product')),
                ('markup_percentage', models.DecimalField(decimal_places=2, default=0.15, max_digits=4)),
            ],
            bases=('pricing.product',),
        ),
        migrations.CreateModel(
            name='SeasonalProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.product')),
                ('seasonal_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
            bases=('pricing.product',),
        ),
        migrations.CreateModel(
            name='FixedAmountDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.discount')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=('pricing.discount',),
        ),
        migrations.CreateModel(
            name='PercentageDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.discount')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            bases=('pricing.discount',),
        ),
        migrations.CreateModel(
            name='TieredDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pricing.discount')),
                ('tiers', models.JSONField(default=dict)),
            ],
            bases=('pricing.discount',),
        ),
    ]