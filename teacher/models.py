from django.db import models
from account.models import User 


class TeacherModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='teacher')
    experience=models.PositiveSmallIntegerField(default=0)
    TeachingArea=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ('experience',)

