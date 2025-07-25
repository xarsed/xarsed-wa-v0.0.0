# Generated by Django 5.1.7 on 2025-07-20 09:08

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
                ('Title', models.CharField(max_length=150, unique=True)),
                ('Content', models.TextField()),
                ('Description', models.CharField(max_length=200)),
                ('Keywords', models.CharField(max_length=200)),
            ],
        ),
    ]
