# Generated by Django 3.0.8 on 2020-07-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0008_auto_20200718_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='iscorrect',
            field=models.BooleanField(default=False),
        ),
    ]
