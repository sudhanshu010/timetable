# Generated by Django 2.2b1 on 2019-04-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]