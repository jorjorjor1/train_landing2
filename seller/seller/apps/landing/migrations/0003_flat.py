# Generated by Django 2.2.7 on 2019-11-17 20:07

from django.db import migrations, models
import landing.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20191113_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=20, null=True, verbose_name='Цена')),
                ('pic', stdimage.models.StdImageField(blank=True, null=True, upload_to=landing.models.get_image_path)),
            ],
        ),
    ]
