# Generated by Django 3.0 on 2020-12-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('standard', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('mobile_no_p1', models.BigIntegerField()),
                ('mobile_no_p2', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
