from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=12)
    description=models.TextField()
def __str__(self):
    return f'message from {self.name}'
