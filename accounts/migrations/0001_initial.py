# Generated by Django 3.2.6 on 2021-08-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('movies_watched', models.ManyToManyField(null=True, to='newsfeed.Movies')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]