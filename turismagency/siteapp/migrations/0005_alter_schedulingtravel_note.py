# Generated by Django 3.2.15 on 2023-06-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0004_schedulingtravel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulingtravel',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
