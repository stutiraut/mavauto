# Generated by Django 2.1.1 on 2020-02-12 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20200212_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
