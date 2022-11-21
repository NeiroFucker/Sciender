# Generated by Django 4.1.3 on 2022-11-21 12:05

import ChatApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='AuthApp.scienderuser')),
            ],
        ),
        migrations.CreateModel(
            name='ScienderChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('background', models.ImageField(default=ChatApp.models.backgroundUploadPath, upload_to=ChatApp.models.backgroundDefaultImage)),
                ('messages', models.ManyToManyField(blank=True, related_name='messages', to='ChatApp.chatmessage')),
                ('users', models.ManyToManyField(related_name='users', to='AuthApp.scienderuser')),
            ],
        ),
    ]
