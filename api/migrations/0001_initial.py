# Generated by Django 4.0.4 on 2022-05-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=155)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]