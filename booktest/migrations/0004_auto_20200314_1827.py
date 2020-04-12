# Generated by Django 2.0 on 2020-03-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20200216_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='身高'),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='体重'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='userdynamic',
            name='img',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]