# Generated by Django 4.0.4 on 2022-06-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lulu_alerts', '0008_notifications_courier_response_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='sent_time',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='complete_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lulu_alerts.notif_origin'),
        ),
    ]
