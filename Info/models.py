from django.db import models

# Create your models here.

class Student(models.Model):
    std_no = models.IntegerField(unique=True)
    std_name = models.CharField(max_length=50)
    std_major = models.CharField(max_length=10)
    std_email = models.EmailField(max_length=30)

    def __str__(self):
        return str(self.std_no) + "-" + self.std_name

class Address(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    city = models.CharField(max_length=15)
    road = models.CharField(max_length=6)
    house = models.CharField(max_length=3)

    def __str__(self):
        return "H#" + self.house + ", " + "R#" + self.road + ", " + "City: " + self.city