# Generated by Django 2.2.2 on 2021-01-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_school_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=200),
        ),
    ]