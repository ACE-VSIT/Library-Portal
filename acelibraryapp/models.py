from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

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


'''
class User(models.Model):

    #enroll_number(foreign key), date of joining, ifACE, ifCore, domain , contact

    enroll_number = models.ForeignKey(Student)
    join_date = models.DateTimeField(null=True)
    domain_choices= (('a','Programming'),('b','Web Development'),('c','Graphic Desgning'),('d','A/V Editing'),('e','Other'))

    domain = models.CharField(max_length=1,choices = domain_choices)


class Tasks(models.Model):
    
    title = models.CharField(max_length=69)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    approval_status = models.BooleanField(default=False)
    solution =  models.TextField(blank=True,null=True)            

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __unicode__(self) :
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


class Categories(models.Model):


    category = models.CharField(primary_key=True,max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['category']


    def __str__(self) :
        return self.category


class Resources(models.Model):

    #category,url,topic,description 
    Category = models.ForeignKey('Categories')
    Course = models.CharField(max_length=30)
    Difficulty = models.IntegerField(default=1,validators=[MaxValueValidator(10), MinValueValidator(1)])  
    Description = models.TextField(max_length=50)
    URL = models.CharField(max_length=50)
    Author = models.CharField(max_length=30)
    approval_status = models.BooleanField(default=False)

 
    def __unicode__(self) :
        return self.Course

#ds



'''
class Solutions(models.Model)
    #Task if ( foreign key), solution , submitted by(defaut shud be autehnticated user),date_of submission
'''

class Event(models.Model):
    
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Attendance(models.Model):

    event_id = models.ForeignKey('Event')
    member_choices= (('a','Ashish'),('b','Gaurav'),('c','Aditya'),('d','Coder'),('e','Paan'))
    attended = MultiSelectField(choices=member_choices, max_choices=3)
    #name = models.CharField(max_length=200)     #Name of member
    #events = models.CharField(max_length=1000)  # Comma separated list of event codes
    #attendance =  models.PositiveIntegerField(default=0)




