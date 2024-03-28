from rest_framework import serializers
from .models import CourseModel
from teacher.models import TeacherModel
from teacher.serializers import TeacherSerializer
from category.serializers import CategorySerializer
from category.models import CategoryModel

class CourseSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=CourseModel
        fields=['id','name','duration','seat']
    
    

