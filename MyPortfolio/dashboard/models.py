from django.db import models

class Hero(models.Model):
    smHead=models.CharField(max_length=50)
    Head=models.CharField(max_length=50)
    Head_img=models.FileField(upload_to='',max_length=100,null=True)
    Head_Desc=models.TextField()
    Head_link1=models.CharField(max_length=90)
    Head_link2=models.CharField(max_length=90)
    Head_link3=models.CharField(max_length=90)
    Head_link4=models.CharField(max_length=90)
    Head_link5=models.CharField(max_length=90)
    Mail=models.CharField(max_length=90)

class About_Me(models.Model):
    about_head=models.CharField(max_length=90)
    about_img=models.FileField(upload_to='',max_length=90,null=True)
    about_text=models.TextField()

class Services(models.Model):
    Card_img=models.FileField(upload_to='',max_length=60,null=True)
    Card_hd=models.CharField(max_length=90)

class Education(models.Model):
    Course=models.CharField(max_length=90)
    Department=models.CharField(max_length=150)
    Year=models.CharField(max_length=150)

class lenguage(models.Model):
    language_img=models.FileField(upload_to='',max_length=70,null=True)

class project(models.Model):
    pro_img=models.FileField(upload_to='',max_length=70,null=True)
    pro_detail=models.TextField(max_length=220)
    pro_link=models.CharField(max_length=90)
    
class testimonial(models.Model):
    test_img=models.FileField(upload_to='',max_length=70,null=True)
    test_text=models.TextField()

class touch(models.Model):
    t_email=models.CharField(max_length=50)
    t_cnt=models.CharField(max_length=25)
    t_loc=models.CharField(max_length=90)
# Create your models here.
