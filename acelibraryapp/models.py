from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):

    #name,enrollNumebr,email_id
    name = models.CharField(max_length=50)
    enroll_number = models.PositiveIntegerField(primary_key=True)
    email_id = models.EmailField(max_length=50,unique=True)

    def __unicode__(self):
        return self.name

    class Meta :
        ordering = ['name']

'''
id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `oauth_uid` bigint(20) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `api` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `pic_square` varchar(255) NOT NULL,
  `course` varchar(10) DEFAULT NULL,
  `semester` varchar(10) DEFAULT NULL,
  `section` varchar(2) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `valid` int(2) DEFAULT '0',



'''

class AceMembers(models.Model):

    id = models.IntegerField(primary_key=True,default=0)
    oauth_uid = models.PositiveIntegerField()
    name = models.CharField(max_length =255, blank=False)
    api = models.CharField(max_length =255,blank=False)
    email = models.CharField(max_length =255,blank=False)
    gender = models.CharField(max_length =50,blank=False)
    pic_square = models.CharField(max_length =255,blank=False)
    course = models.CharField(max_length =10,null=True)
    semester = models.CharField(max_length =10,null=True)
    section = models.CharField(max_length =2,null=True)
    phone = models.CharField(max_length =12,null=True)
    valid = models.PositiveIntegerField(default=0)









class User(models.Model):

    #enroll_number(foreign key), date of joining, ifACE, ifCore, domain , contact

    enroll_number = models.ForeignKey(Student)
    join_date = models.DateTimeField(null=True)
    ifACE = models.BooleanField()
    ifCore = models.BooleanField()
    domain_choices= (('a','Programming'),('b','Web Development'),('c','Graphic Desgning'),('d','A/V Editing'),('e','Other'))

    domain = models.CharField(max_length=1,choices = domain_choices)



class Tasks(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approval_status = models.BooleanField(default=False)
    solution =  models.TextField(blank=True,null=True)            

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def _str_(self):
        return self.title


class Events(models.Model):


    ID = models.TextField(primary_key = True)
    date = models.DateTimeField(default=timezone.now)
    name = models.TextField(max_length=30)
    description = models.TextField(blank=True,null=True)

    def __init(self):
        self.date=timezone.now()
        self.save()

    def _str_(self):
        return self.name



class Resources(models.Model):

    #category,url,topic,description 
    course = models.CharField(max_length=30)  
    couse_diff = models.CharField(max_length=10)
    couse_des = models.TextField(max_length=50)
    link = models.CharField(max_length=50)
    course_type =models.CharField(max_length=20)
    course_author = models.CharField(max_length=30)
    approval_status = models.BooleanField(default=False)




'''
class Attendance(models.Model):

    #user_id(foreign key),#event_id(foreign key), attendance(String)



class Solutions(models.Model)
    #Task if ( foreign key), solution , submitted by(defaut shud be autehnticated user),date_of submission




'''




