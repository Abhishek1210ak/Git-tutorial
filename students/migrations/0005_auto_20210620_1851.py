# Generated by Django 3.2.4 on 2021-06-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_teacher_my_class_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='my_class_teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='my_class_teacher',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_class_teacher', to='students.teacher'),
        ),
    ]
