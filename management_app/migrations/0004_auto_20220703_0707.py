# Generated by Django 3.0.7 on 2022-07-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0003_auto_20220703_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionyearmodel',
            name='session_end_year',
        ),
        migrations.AddField(
            model_name='sessionyearmodel',
            name='event_name',
            field=models.CharField(default='UNKNOWN', max_length=255),
        ),
        migrations.AddField(
            model_name='sessionyearmodel',
            name='hadm_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management_app.Admission'),
        ),
    ]
