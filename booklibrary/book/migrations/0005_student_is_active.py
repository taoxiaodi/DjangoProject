# Generated by Django 2.2 on 2019-04-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_textinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
