from django.db import models

# Create your models here.

class books(models.Model):
    course_name=models.TextField(max_length=100)
    book_name=models.TextField(max_length=100)
    book_code=models.TextField(max_length=100,null=True)
    auther=models.TextField(max_length=300,null=True)
    semester=models.TextField(max_length=100)
    eng_branch=models.TextField(max_length=100)

    def __str__(self):
        return self.course_name
    
class courses(models.Model):
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    
class course_offer_university(models.Model):
    university_name=models.CharField(max_length=100)
    course_offered=models.ManyToManyField(courses,related_name='courses')



