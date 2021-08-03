# Generated by Django 3.2.6 on 2021-08-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('guid', models.TextField(max_length=500, null=True)),
                ('guid_is_perma_link', models.BooleanField(default=False)),
                ('link', models.TextField(max_length=1000)),
                ('pubDate', models.DateTimeField()),
            ],
        ),
    ]
