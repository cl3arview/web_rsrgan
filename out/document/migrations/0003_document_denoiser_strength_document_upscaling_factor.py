# Generated by Django 4.2.1 on 2023-05-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_ai_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Denoiser_strength',
            field=models.CharField(default=0.5, max_length=100),
        ),
        migrations.AddField(
            model_name='document',
            name='Upscaling_factor',
            field=models.CharField(default=2, max_length=100),
        ),
    ]
