# Generated by Django 4.0.5 on 2022-06-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("researchers", "0006_researcherpage_facebook_link_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="researcherpage",
            old_name="contact_name",
            new_name="name",
        ),
    ]
