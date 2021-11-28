# Generated by Django 3.2.4 on 2021-08-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Grocery', 'Grocery'), ('Rice', 'Rice'), ('Fish', 'Fish'), ('Oil', 'Oil'), ('Vegetables', 'Vegetables'), ('Beverages', 'Beverages'), ('Meat', 'Meat'), ('Bakery & Snacks', 'Bakery & Snacks'), ('Dairy', 'Dairy'), ('Household & Clean', 'Household & Clean')], max_length=50),
        ),
    ]
