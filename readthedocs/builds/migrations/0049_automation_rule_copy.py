# Generated by Django 3.2.18 on 2023-03-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("builds", "0048_add_build_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="automationrulematch",
            name="action",
            field=models.CharField(
                choices=[
                    ("activate-version", "Activate version"),
                    ("hide-version", "Hide version"),
                    ("make-version-public", "Make version public"),
                    ("make-version-private", "Make version private"),
                    ("set-default-version", "Set version as default"),
                    ("delete-version", "Delete version"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="versionautomationrule",
            name="action",
            field=models.CharField(
                choices=[
                    ("activate-version", "Activate version"),
                    ("hide-version", "Hide version"),
                    ("make-version-public", "Make version public"),
                    ("make-version-private", "Make version private"),
                    ("set-default-version", "Set version as default"),
                    ("delete-version", "Delete version"),
                ],
                help_text="Action to apply to matching versions",
                max_length=32,
                verbose_name="Action",
            ),
        ),
    ]