# Generated by Django 4.1.5 on 2023-02-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
