# Generated by Django 2.0.5 on 2018-05-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0018_auto_20180528_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='language',
            field=models.IntegerField(),
        ),
    ]
