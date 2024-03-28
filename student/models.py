from django.db import models
from account.models import User

class StudentModel(models.Model):
    user=models.OneToOneField(User,related_name="student",on_delete=models.CASCADE)
    department=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username
    
