# Generated by Django 5.0.4 on 2024-04-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csctest', '0004_exhibit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit',
            name='additional_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
