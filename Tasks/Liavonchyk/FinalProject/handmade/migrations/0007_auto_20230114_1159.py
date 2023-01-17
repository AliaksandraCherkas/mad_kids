# Generated by Django 3.2.16 on 2023-01-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handmade', '0006_auto_20230114_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='purchase_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='purchase_place',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='material',
            name='nominal_amount',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='purchase_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='purchase_place',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
