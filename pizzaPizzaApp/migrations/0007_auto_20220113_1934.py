# Generated by Django 2.2.25 on 2022-01-13 18:34

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaPizzaApp', '0006_auto_20220111_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='username',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
