# Generated by Django 2.2.25 on 2022-01-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaPizzaApp', '0007_auto_20220113_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='username',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
