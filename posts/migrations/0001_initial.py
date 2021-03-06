# Generated by Django 3.0.2 on 2020-01-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('topic', models.CharField(choices=[('air', 'Air'), ('water', 'Water'), ('food', 'Food'), ('housing', 'Housing'), ('health', 'Health'), ('education', 'Education'), ('transportation', 'Transportation'), ('sexuality', 'Sexuality')], max_length=20)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100)),
                ('author', models.CharField(max_length=80)),
                ('keywords', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=250)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='posts/images/%Y/%M')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_on', 'author', 'topic'),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=80)),
                ('text', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
            options={
                'ordering': ('posted_on', 'post', 'writer'),
            },
        ),
    ]
