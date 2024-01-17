# Generated by Django 3.2.21 on 2024-01-10 10:19

from django.db import migrations, models
import nautobot_ssot.models


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_ssot", "0007_replace_dashed_custom_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sync",
            name="diff",
            field=models.JSONField(blank=True, encoder=nautobot_ssot.models.DiffJSONEncoder),
        ),
        migrations.AlterField(
            model_name="synclogentry",
            name="diff",
            field=models.JSONField(blank=True, encoder=nautobot_ssot.models.DiffJSONEncoder, null=True),
        ),
    ]
