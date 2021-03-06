# Generated by Django 3.0.2 on 2020-01-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=80)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('send_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('send_date', 'name'),
            },
        ),
    ]
