# Generated by Django 2.2.25 on 2022-01-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaPizzaApp', '0002_auto_20220104_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='pizzaModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaPizzaApp.PizzaModel'),
        ),
    ]
