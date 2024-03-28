from student.models import StudentModel
from student.serializers import StudentSerializer
from teacher.models import TeacherModel
from teacher.serializers import TeacherSerializer
from course.models import CourseModel
from course.serializers import CourseSerializer
from category.models import CategoryModel
from category.serializers import CategorySerializer
from rest_framework import serializers
from .models import EnrollmentModel

class EnrollmentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = EnrollmentModel
        fields = '__all__'
