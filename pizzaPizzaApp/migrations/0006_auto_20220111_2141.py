# Generated by Django 2.2.25 on 2022-01-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaPizzaApp', '0005_auto_20220111_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='email',
        ),
        migrations.AddField(
            model_name='comentario',
            name='username',
            field=models.CharField(default='username', max_length=100),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='descripcion',
            field=models.CharField(max_length=2000),
        ),
    ]
