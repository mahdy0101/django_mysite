# Generated by Django 4.1.7 on 2023-05-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0006_produitnc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
