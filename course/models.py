from django.db import models
from teacher.models import TeacherModel
from category.models import CategoryModel
class CourseModel(models.Model):
   
    name=models.CharField(max_length=200,unique=True)
    duration=models.IntegerField()
    seat=models.IntegerField()

    def __str__(self) -> str:
        return self.name


