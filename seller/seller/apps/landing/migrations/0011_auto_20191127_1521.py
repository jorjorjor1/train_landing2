# Generated by Django 2.2.7 on 2019-11-27 12:21

from django.db import migrations, models
import landing.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20191126_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatAqvarel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=20, null=True, verbose_name='Цена')),
                ('pic', stdimage.models.StdImageField(blank=True, null=True, upload_to=landing.models.get_image_path)),
            ],
        ),
        migrations.RenameModel(
            old_name='Flat',
            new_name='FlatRodonit',
        ),
    ]