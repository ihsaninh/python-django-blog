# Generated by Django 2.2 on 2019-05-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='gambar',
            field=models.CharField(default='artikel', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artikel',
            name='kategori',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]