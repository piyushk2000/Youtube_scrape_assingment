# Generated by Django 4.1.1 on 2022-09-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIData',
            fields=[
                ('vid_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('vid_title', models.CharField(max_length=500)),
                ('vid_publishDate', models.CharField(max_length=50)),
                ('vid_description', models.CharField(max_length=5000)),
                ('logo_url', models.CharField(max_length=50)),
            ],
        ),
    ]
