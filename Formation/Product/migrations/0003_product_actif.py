# Generated by Django 5.0.1 on 2024-02-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_delete_person_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
