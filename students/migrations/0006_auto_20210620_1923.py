# Generated by Django 3.2.4 on 2021-06-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20210620_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='my_class_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_teacher_roll',
            field=models.CharField(default='FECOMPD', max_length=10),
            preserve_default=False,
        ),
    ]
