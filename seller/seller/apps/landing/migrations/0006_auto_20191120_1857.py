# Generated by Django 2.2.7 on 2019-11-20 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20191120_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infotext',
            old_name='h1_text_aligh',
            new_name='h1_text_align',
        ),
    ]