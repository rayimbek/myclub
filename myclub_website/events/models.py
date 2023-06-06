from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Student(models.Model):
	user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
	name = models.CharField('Name' ,max_length = 120)
	surname = models.CharField('Surname' ,null = True,max_length = 120)
	country = models.CharField('Country' ,null = True,max_length = 120)
	city  = models.CharField('City' ,null = True,max_length = 120)
	profile_pic = models.ImageField(default = "profile1.png",null = True, blank = True, upload_to = "profile/")
	
	
	def __str__(self):
		return self.name


class Subject(models.Model):
	student = models.ForeignKey(Student ,blank=True, null = True ,on_delete= models.CASCADE)
	SubjectName = models.CharField('Subject Name' ,max_length = 120)
	data_created = models.DateTimeField(auto_now_add = True, null = True)
	TimeRemaining = models.DateTimeField('Deadline')

	def __str__(self):
		return self.SubjectName

	@property
	def days_still(self):
		today = date.today()
		days = self.TimeRemaining.date()  - today
		days_str = str(days).split(",",1)[0]
		return days_str


class Club(models.Model):
	name  = models.CharField('Club name',max_length = 120)
	description = models.TextField(blank=True)
	mission = models.TextField(blank=True)
	members = models.ManyToManyField(Student, blank = True)
	club_image = models.ImageField(null = True, blank = True, upload_to = "images/")
	image2 = models.ImageField(null = True, blank = True, upload_to = "images/")
	data_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):	
		return self.name


class Resource(models.Model):
	STATUS = (
		('Textbooks','Textbooks'),
		('Online Courses','Online Courses'),
		('Websites and Blogs','Websites and Blogs'),
		('Math Forums','Math Forums'),
		)

	name  = models.CharField('Resource name',max_length = 120)
	link = models.URLField('Website Address' ,max_length = 120)
	status = models.CharField(max_length = 200,null = True, choices= STATUS)

	def __str__(self):
		return self.name



class Videoresource(models.Model):
	STATUS = (
		('YouTube Channels','YouTube Channels'),
		('MIT OpenCourseWare','MIT OpenCourseWare'),
		)

	name  = models.CharField('Resource name',max_length = 120)
	link = models.URLField('Website Address' ,max_length = 120)
	status = models.CharField(max_length = 200,null = True, choices= STATUS)

	def __str__(self):
		return self.name


class Course(models.Model):
	name  = models.CharField('Course name',max_length = 120)
	introduction = models.TextField(blank=True)
	studytips = models.TextField(blank=True)
	resources = models.ManyToManyField(Resource,blank=True)
	videoresources = models.ManyToManyField(Videoresource,blank=True)
	conclusion = models.TextField(blank=True)
	course_image = models.ImageField(null = True, blank = True, upload_to = "images/")
	data_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name		

"""
class Venue(models.Model):
	name = models.CharField('Venue Name' ,max_length = 120)
	address = models.CharField(max_length = 300)
	zip_code = models.CharField('Zip Code' ,max_length = 15)
	phone = models.CharField('Contact Phone' ,max_length = 25)
	web = models.URLField('Website Address' ,max_length = 120)
	email_address = models.EmailField('Email Address')

	def __str__(self):
		return self.name


class MyClubUser(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.CharField('User Email', max_length = 30)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Event(models.Model):
	name  = models.CharField('Event name',max_length = 120)
	event_date = models.DateTimeField('Event date')
	venue =	models.ForeignKey(Venue ,blank=True, null = True ,on_delete= models.CASCADE)
	#venue =models.CharField(max_length = 120)
	manager = models.CharField(max_length = 160)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser, blank = True)

	def __str__(self):
		return self.name
		"""
