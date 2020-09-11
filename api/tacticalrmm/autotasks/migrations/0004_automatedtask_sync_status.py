# Generated by Django 3.1.1 on 2020-09-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotasks', '0003_automatedtask_script_args'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatedtask',
            name='sync_status',
            field=models.CharField(choices=[('synced', 'Synced With Agent'), ('notsynced', 'Waiting On Agent Checkin'), ('pendingdeletion', 'Pending Deletion on Agent')], default='notsynced', max_length=100),
        ),
    ]
