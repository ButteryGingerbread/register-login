# Generated by Django 5.0.6 on 2024-07-05 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayMenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=200)),
                ('menu_ingredients', models.TextField()),
                ('menu_instructions', models.TextField()),
                ('menu_category', models.CharField(max_length=100)),
            ],
        ),
    ]
