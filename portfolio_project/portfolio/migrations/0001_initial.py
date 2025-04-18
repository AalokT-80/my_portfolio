# Generated by Django 5.1.7 on 2025-03-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('issuing_org', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('certificate_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=200)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('demo_image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('category', models.CharField(choices=[('Data Analysis', 'Data Analysis'), ('Machine Learning', 'Machine Learning'), ('Visualization', 'Visualization')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Data Analysis', 'Data Analysis'), ('Machine Learning', 'Machine Learning'), ('Visualization', 'Visualization'), ('Tools', 'Tools')], max_length=50)),
            ],
        ),
    ]
