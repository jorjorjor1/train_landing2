# Generated by Django 2.2.7 on 2019-11-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_infotext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infotext',
            old_name='text_content',
            new_name='h1_content',
        ),
        migrations.RenameField(
            model_name='infotext',
            old_name='font_size',
            new_name='h1_font_size',
        ),
        migrations.AddField(
            model_name='infotext',
            name='h1_text_aligh',
            field=models.CharField(default='center', max_length=15),
        ),
        migrations.AddField(
            model_name='infotext',
            name='h1_text_color',
            field=models.CharField(default='black', max_length=50),
        ),
    ]
