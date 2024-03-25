# Generated by Django 5.0.3 on 2024-03-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=5000)),
                ('education', models.CharField(max_length=5000)),
                ('work_experience', models.CharField(max_length=5000)),
                ('skill', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('description', models.CharField(max_length=5000)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]