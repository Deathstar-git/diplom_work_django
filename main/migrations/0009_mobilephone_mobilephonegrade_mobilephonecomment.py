# Generated by Django 4.1.7 on 2023-05-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_fridgegrade_remove_fridge_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('img_url', models.TextField(blank=True, null=True, verbose_name='Ссылка на картинку')),
                ('total_useful_volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='Общий полезный обьем')),
            ],
            options={
                'verbose_name': 'Мобильный телефон',
                'verbose_name_plural': 'Мобильные телефоны',
            },
        ),
        migrations.CreateModel(
            name='MobilePhoneGrade',
            fields=[
                ('negative_count', models.IntegerField(default=0)),
                ('neutral_count', models.IntegerField(default=0)),
                ('positive_count', models.IntegerField(default=0)),
                ('total_grade', models.IntegerField(default=0)),
                ('phone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.mobilephone')),
            ],
        ),
        migrations.CreateModel(
            name='MobilePhoneComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('grade', models.IntegerField(null=True)),
                ('phone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.mobilephone')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
