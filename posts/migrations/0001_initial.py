# Generated by Django 3.0.2 on 2020-01-23 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('login', models.CharField(max_length=48)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('img', models.ImageField(upload_to='media/img')),
                ('text', models.CharField(max_length=256)),
                ('data', models.DateTimeField(default=datetime.datetime(2020, 1, 23, 22, 53, 54, 436426))),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
            ],
        ),
    ]
