# Generated by Django 4.2.6 on 2023-10-20 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0027_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='course',
        ),
        migrations.AddField(
            model_name='test',
            name='lesson',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentication.lesson'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
