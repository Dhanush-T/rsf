# Generated by Django 4.0.5 on 2022-10-05 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('researchers', '0011_alter_researcherpage_orcid_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researcherpage',
            old_name='intrests',
            new_name='interests',
        ),
    ]