# Generated by Django 2.2.7 on 2019-11-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_flat'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(max_length=2000)),
                ('font_size', models.IntegerField(default=18)),
            ],
        ),
    ]
