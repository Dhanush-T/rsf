# Generated by Django 4.0.5 on 2022-06-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchers', '0003_seminarandviva_speaker'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminarandviva',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Viva Voice', 'Viva Voice')], default='Seminar', max_length=225),
        ),
        migrations.AlterField(
            model_name='researcherpage',
            name='department',
            field=models.CharField(choices=[('', ''), ('Architecture', 'Architecture'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Electrical Engineering', 'Electrical Engineering'), ('Environmental Engineering', 'Environmental Engineering'), ('Industrial Engineering', 'Industrial Engineering'), ('Materials Science', 'Materials Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Nuclear Engineering', 'Nuclear Engineering'), ('Other', 'Other')], default='Professor', max_length=225),
        ),
    ]
