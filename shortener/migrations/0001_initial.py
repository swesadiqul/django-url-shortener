# Generated by Django 3.2 on 2022-12-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'URL Shortener',
                'ordering': ['-id'],
            },
        ),
    ]
