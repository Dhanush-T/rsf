# Generated by Django 4.0.5 on 2022-06-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchers', '0002_seminarandviva'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminarandviva',
            name='speaker',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
