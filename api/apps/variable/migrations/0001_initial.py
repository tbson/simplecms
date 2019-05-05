# Generated by Django 2.2 on 2019-05-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=60, unique=True)),
                ('value', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'variables',
                'ordering': ['-id'],
            },
        ),
    ]
