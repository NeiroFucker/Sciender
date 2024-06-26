# Generated by Django 4.1.3 on 2022-12-04 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoreApp', '0001_initial'),
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScienderStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to='AuthApp.scienderuser')),
            ],
        ),
        migrations.CreateModel(
            name='ScienderScienceWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('academic_title', models.CharField(blank=True, max_length=255)),
                ('academic_degree', models.CharField(blank=True, max_length=255)),
                ('qualifying_links', models.ManyToManyField(blank=True, to='CoreApp.worklink')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worker_user', to='AuthApp.scienderuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScienderScienceTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('academic_title', models.CharField(blank=True, max_length=255)),
                ('academic_degree', models.CharField(blank=True, max_length=255)),
                ('qualifying_links', models.ManyToManyField(blank=True, to='CoreApp.worklink')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_user', to='AuthApp.scienderuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScienderGraduateStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='graduate_user', to='AuthApp.scienderuser')),
            ],
        ),
    ]
