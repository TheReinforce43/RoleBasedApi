# Generated by Django 5.0.3 on 2024-03-10 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('course', '0001_initial'),
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnrollingDate', models.DateTimeField(auto_now_add=True)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category_enroll', to='category.categorymodel')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_enroll', to='course.coursemodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_enroll', to='student.studentmodel')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_enroll', to='teacher.teachermodel')),
            ],
        ),
    ]
