# Generated by Django 2.2.7 on 2019-11-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20191120_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotext',
            name='text_content',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
