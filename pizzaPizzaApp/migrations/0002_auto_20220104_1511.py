# Generated by Django 2.2.25 on 2022-01-04 14:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaPizzaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('valoracion', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaModel_id', models.IntegerField()),
                ('nombre', models.CharField(default='default', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.AddField(
            model_name='comentario',
            name='pizzaModel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizzaPizzaApp.PizzaModel'),
        ),
    ]
