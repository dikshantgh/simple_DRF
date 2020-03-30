# Generated by Django 3.0.4 on 2020-03-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50)),
            ],
        ),
    ]
