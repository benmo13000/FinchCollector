# Generated by Django 4.2.6 on 2023-11-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
    ]