# Generated by Django 2.2.7 on 2019-11-12 21:54

from django.db import migrations, models
import landing.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='pic',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=landing.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.TextField(help_text='Сама новость', max_length=300),
        ),
    ]
