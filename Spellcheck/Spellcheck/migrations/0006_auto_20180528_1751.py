# Generated by Django 2.0.5 on 2018-05-28 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0005_remove_text_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='author',
            field=models.ForeignKey(default='anonymous', on_delete=django.db.models.deletion.CASCADE, to='Spellcheck.User'),
        ),
        migrations.AddField(
            model_name='text',
            name='language',
            field=models.IntegerField(default=1),
        ),
    ]
