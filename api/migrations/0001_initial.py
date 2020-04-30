# Generated by Django 3.0.5 on 2020-04-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=20)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('thumbnail', models.CharField(max_length=100)),
            ],
        ),
    ]
