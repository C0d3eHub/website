# Generated by Django 5.1.3 on 2024-11-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_tender_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercontent',
            name='right_logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
