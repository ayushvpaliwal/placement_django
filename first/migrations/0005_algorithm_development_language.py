# Generated by Django 3.2.3 on 2021-09-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20210926_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='algorithm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='development',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
            ],
        ),
    ]
