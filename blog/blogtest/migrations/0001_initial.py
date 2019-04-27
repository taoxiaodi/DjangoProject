# Generated by Django 2.2 on 2019-04-25 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('create', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField()),
                ('digest', models.TextField()),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
                ('la', models.ManyToManyField(to='blogtest.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='classifyid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogtest.Classify'),
        ),
    ]
