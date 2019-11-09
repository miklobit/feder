# Generated by Django 1.11.10 on 2018-02-27 19:08

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


def update_record_field(apps, schema_editor):
    Record = apps.get_model("records", "Record")
    Letter = apps.get_model("letters", "Letter")
    db_alias = schema_editor.connection.alias
    for letter in Letter.objects.using(db_alias).filter(record=None).all():
        record = Record.objects.create(case=letter.case, created=letter.created)
        letter.record = record
        letter.save(update_fields=["record"])


class Migration(migrations.Migration):

    dependencies = [("records", "0001_initial"), ("letters", "0016_auto_20180227_1907")]

    operations = [
        migrations.AddField(
            model_name="letter",
            name="record",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="letters_letter_related",
                related_query_name="letters_letters",
                to="records.Record",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="letter",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, verbose_name="created"
            ),
        ),
        migrations.AlterField(
            model_name="letter",
            name="modified",
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name="modified"
            ),
        ),
        migrations.RunPython(update_record_field),
        migrations.AlterField(
            model_name="letter",
            name="record",
            field=models.ForeignKey(
                default=1,
                null=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="letters_letter_related",
                related_query_name="letters_letters",
                to="records.Record",
            ),
            preserve_default=False,
        ),
    ]
