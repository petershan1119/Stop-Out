# Generated by Django 2.0.2 on 2018-02-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webtoon_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
