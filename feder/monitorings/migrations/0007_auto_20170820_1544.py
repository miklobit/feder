# Generated by Django 1.11.4 on 2017-08-20 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("monitorings", "0006_monitoring_subject")]

    operations = [
        migrations.AlterModelOptions(
            name="monitoring",
            options={
                "ordering": ["created"],
                "permissions": (
                    ("add_questionary", "Can add questionary"),
                    ("change_questionary", "Can change questionary"),
                    ("delete_questionary", "Can delete questionary"),
                    ("add_case", "Can add case"),
                    ("change_case", "Can change case"),
                    ("delete_case", "Can delete case"),
                    ("add_task", "Can add task"),
                    ("change_task", "Can change task"),
                    ("delete_task", "Can delete task"),
                    ("add_letter", "Can add letter"),
                    ("reply", "Can reply"),
                    ("add_draft", "Add reply draft"),
                    ("change_letter", "Can change task"),
                    ("delete_letter", "Can delete letter"),
                    ("view_alert", "Can view alert"),
                    ("change_alert", "Can change alert"),
                    ("delete_alert", "Can delete alert"),
                    ("manage_perm", "Can manage perms"),
                    ("select_survey", "Can select answer"),
                    ("view_log", "Can view logs"),
                ),
                "verbose_name": "Monitoring",
                "verbose_name_plural": "Monitoring",
            },
        )
    ]
