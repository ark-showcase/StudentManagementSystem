# Generated by Django 4.1.3 on 2022-11-24 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=15)),
                ('road', models.CharField(max_length=6)),
                ('house', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_no', models.IntegerField(unique=True)),
                ('std_name', models.CharField(max_length=50)),
                ('std_major', models.CharField(max_length=10)),
                ('std_email', models.EmailField(max_length=30)),
                ('std_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Info.address')),
            ],
        ),
    ]
