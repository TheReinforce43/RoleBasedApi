from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self) -> str:
        return self.name
