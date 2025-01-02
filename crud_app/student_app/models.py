from django.db import models

# Create your models here.
class student(models.Model):
    nic = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    resident = models.CharField(max_length=50)
    banner = models.ImageField(default='student.jpg', blank=True)

    def __str__(self):
        return self.name
    