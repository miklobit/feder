# Generated by Django 1.11.7 on 2018-01-16 22:05

from django.db import migrations, models


def update_draft_status(apps, schema_editor):
    Letter = apps.get_model("letters", "Letter")
    Letter.objects.filter(author_user__isnull=False).exclude(eml="").update(
        is_draft=False
    )
    Letter.objects.filter(author_user__isnull=True).update(is_draft=False)


class Migration(migrations.Migration):

    dependencies = [("letters", "0010_auto_20180112_1721")]

    operations = [
        migrations.AddField(
            model_name="letter",
            name="is_draft",
            field=models.BooleanField(default=True, verbose_name="Is draft?"),
        ),
        migrations.RunPython(update_draft_status),
    ]
