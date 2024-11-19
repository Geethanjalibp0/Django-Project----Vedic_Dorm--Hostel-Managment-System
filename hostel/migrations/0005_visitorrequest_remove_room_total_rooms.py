# Generated by Django 5.0.7 on 2024-07-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_remove_student_mphn_no_alter_student_fphn_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
                ('visitor_name', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=50)),
                ('ph_no', models.CharField(max_length=15)),
                ('visit_date', models.DateField()),
                ('visit_time', models.TimeField()),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='total_rooms',
        ),
    ]