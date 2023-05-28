# Generated by Django 4.1.7 on 2023-05-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_fridge_grade'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='FridgeComment',
        ),
        migrations.AddField(
            model_name='fridge',
            name='depth',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Глубина'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Габариты (ВхГхШ)'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='package_height',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Высота упаковки'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='package_width',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ширина упаковки'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='total_useful_volume',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Общий полезный обьем'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='total_volume',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Общий обьем'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='useful_volume_freezer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Полезный объем морозильной камеры'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='useful_volume_refrigerator',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Общий полезный обьем холодильной камеры'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='volume_freezer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Объем морозильной камеры'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='volume_refrigerator',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Общий обьем холодильной камеры'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='width',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ширина'),
        ),
    ]
