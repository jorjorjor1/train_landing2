# Generated by Django 2.2.7 on 2019-11-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20191122_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotext',
            name='h1_content',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='h1_font_size',
            field=models.IntegerField(blank=True, default=18),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='h1_text_align',
            field=models.CharField(blank=True, default='center', max_length=15),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='h1_text_color',
            field=models.CharField(blank=True, default='black', max_length=50),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='text_align',
            field=models.CharField(blank=True, default='center', max_length=15),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='text_color',
            field=models.CharField(blank=True, default='black', max_length=50),
        ),
        migrations.AlterField(
            model_name='infotext',
            name='text_font_size',
            field=models.IntegerField(blank=True, default=18),
        ),
    ]
