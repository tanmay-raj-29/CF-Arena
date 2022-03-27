# Generated by Django 4.0 on 2022-03-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('contest_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('contest_duration', models.IntegerField(blank=True, default=120)),
                ('name', models.CharField(default='Codeforces Round #0', max_length=250)),
            ],
        ),
    ]
