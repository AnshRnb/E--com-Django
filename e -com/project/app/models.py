from django.db import models

# Create your models here.




class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    # stu_contact=models.IntegerField()
    # stu_dis=models.CharField(max_length=200)
    # stu_dob=models.DateField(max_length=50)
    # stu_edu=models.CharField(max_length=50)
    # stu_gender=models.CharField(max_length=50)
    # stu_image=models.ImageField(upload_to='images/')
    # stu_document=models.FileField(upload_to='file/')
    stu_password=models.CharField(max_length=50)
    stu_cpassword=models.CharField(max_length=50)