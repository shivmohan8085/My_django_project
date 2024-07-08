from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    working=models.BooleanField()
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)  
    testimonial = models.TextField() 
    # picture = models.ImageField(upload_to='testimonials/')
    picture = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField()  # rating (e.g., 1-5 stars)

    def __str__(self):
        return self.testimonial  # returns the testimonial text as a string representation