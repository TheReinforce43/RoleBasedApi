from django.db import models
from student.models import StudentModel
from teacher.models import TeacherModel
from category.models import CategoryModel
from course.models import CourseModel


class EnrollmentModel(models.Model):

    student=models.ForeignKey(StudentModel, related_name='student_enroll',on_delete=models.CASCADE)
    teacher=models.OneToOneField(TeacherModel, related_name='teacher_enroll',on_delete=models.CASCADE)
    category=models.OneToOneField(CategoryModel, related_name='category_enroll',on_delete=models.CASCADE)
    course=models.OneToOneField(CourseModel, related_name='course_enroll',on_delete=models.CASCADE)
    EnrollingDate=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student} - {self.EnrollingDate}"

    
