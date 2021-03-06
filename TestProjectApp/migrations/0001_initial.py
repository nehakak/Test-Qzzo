# Generated by Django 3.0.4 on 2020-09-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('Age', models.IntegerField(max_length=200)),
                ('Image', models.ImageField(upload_to='test/images/')),
                ('LoginID', models.CharField(max_length=200)),
                ('EmailID', models.CharField(max_length=500)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
