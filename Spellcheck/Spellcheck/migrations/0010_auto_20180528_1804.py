# Generated by Django 2.0.5 on 2018-05-28 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0009_auto_20180528_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Spellcheck.User'),
        ),
    ]
