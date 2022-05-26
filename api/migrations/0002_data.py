# Generated by Django 4.0.4 on 2022-05-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('name', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
