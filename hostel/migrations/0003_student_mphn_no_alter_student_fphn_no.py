# Generated by Django 5.0.6 on 2024-07-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_room_is_occupied'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mphn_no',
            field=models.CharField(default=8754965651, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='fphn_no',
            field=models.CharField(max_length=10),
        ),
    ]
