# Generated by Django 2.2 on 2019-05-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_auto_20190528_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activitye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Intereste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interest', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Skille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.CharField(max_length=264)),
            ],
        ),
    ]
