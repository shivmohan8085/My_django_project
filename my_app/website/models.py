from django.db import models

class Student(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    mo_num = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)


