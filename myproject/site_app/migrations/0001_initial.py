# Generated by Django 2.2 on 2019-05-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=32)),
                ('Email', models.EmailField(max_length=254)),
                ('Reasom', models.CharField(max_length=32)),
                ('Message', models.CharField(max_length=1030)),
            ],
        ),
    ]
