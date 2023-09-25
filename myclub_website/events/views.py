from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from datetime import datetime
from django import template
import calendar
from .forms import *

@login_required(login_url ='login')
def home(request):
	return render(request, 'home.html',{})


@login_required(login_url ='login')
def profile(request):
	if request.user.is_superuser: 
		context = {}
		return render(request, 'profile.html',context)
	else:
		student = Student.objects.get(user=request.user)
		print(student.name)
		context = {'student' : student}
		return render(request, 'profile.html',context)
	

def userCreation(request):
	form = CreateUserForm()
	if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('createstudent')

	context = {'form' : form}
	return render(request, 'userCreation.html',context)

@login_required(login_url ='login')
def accSettings(request):
	if request.user.is_superuser: 
		
		return render(request, 'accsettings.html',{})
	else:
		student  = request.user.student
		form = StudentForm(instance = student)
		if request.method == 'POST':
			form = StudentForm(request.POST, request.FILES,instance = student)
			if form.is_valid():
				form.save()
				return redirect('profile')

		context = {'form' : form }
		return render(request, 'accsettings.html',context)
	
def flash(request):
	name = "Rayimbe"
	return render(request, 'flash.html',{ "first_name": name})

def aituevents(request):
	name = "Rayimbe"
	clubs = Club.objects.all()
	if request.user.is_superuser: 
		return render(request, 'adminpanel/editevent.html',{ "club_list": clubs})	
	else:
		return render(request, 'aituevents.html',{ "club_list": clubs})
 

def editevents(request):
	name = "Rayimbe"
	clubs = Club.objects.all()
	return render(request, 'adminpanel/editevent.html',{ "club_list": clubs})


def createClub(request):
	form = ClubForm();
	if request.method == 'POST':
		form = ClubForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			return redirect('aituevents')
        
	context = {'form' : form }
	return render(request, 'adminpanel/club_form.html',context)

def updateClub(request, pk):
	
	club = Club.objects.get(id = pk)
	form = ClubForm(instance =club);
	if request.method == 'POST':
		form = ClubForm(request.POST, request.FILES,instance = club)
		if form.is_valid():
			form.save()
			return redirect('aituevents')

	context = {'form' : form , 'club' : club}
	return render(request, 'adminpanel/update_club.html',context)	

def deleteClub(request, pk):
	
	club = Club.objects.get(id = pk)
	if request.method == 'POST':
		club.delete()
		return redirect('aituevents')

	context = {'club' : club}
	return render(request, 'adminpanel/delete_club.html',context)		



def createCourse(request):
	form = CourseForm()
	if request.method == 'POST':
		form = CourseForm(request.POST ,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('prepare')
       	 
	context = {'form' : form }
	return render(request, 'adminpanel/course_form.html',context)

def updateCourse(request, pk):
	
	course = Course.objects.get(id = pk)
	form = CourseForm(instance =course);
	if request.method == 'POST':
		form = CourseForm(request.POST, request.FILES,instance = course)
		if form.is_valid():
			form.save()
			return redirect('prepare')

	context = {'form' : form , 'course' : course}
	return render(request, 'adminpanel/update_course.html',context)	

def deleteCourse(request, pk):
	
	course = Course.objects.get(id = pk)
	if request.method == 'POST':
		course.delete()
		return redirect('prepare')

	context = {'course' : course}
	return render(request, 'adminpanel/delete_course.html',context)	


def createVresource(request):
	form = VideoResourceForm()
	if request.method == 'POST':
		form = VideoResourceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('prepare')
       	 
	context = {'form' : form }
	return render(request, 'adminpanel/VideoResource/vresource_form.html',context)

def updateVresource(request, pk):
	
	videoresource = Videoresource.objects.get(id = pk)
	form = VideoResourceForm(instance =videoresource);
	if request.method == 'POST':
		form = VideoResourceForm(request.POST, instance = videoresource)
		if form.is_valid():
			form.save()
			return redirect('prepare')


	context = {'form' : form , 'item' : videoresource}
	return render(request, 'adminpanel/VideoResource/update_vresource.html',context)	

def deleteVresource(request, pk):
	
	videoresource = Videoresource.objects.get(id = pk)
	if request.method == 'POST':
		videoresource.delete()
		return redirect('prepare')

	context = {'item' : videoresource}
	return render(request, 'adminpanel/VideoResource/delete_vresource.html',context)	



def createResource(request):
	form = ResourceForm()
	if request.method == 'POST':
		form = ResourceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('prepare')
       	 
	context = {'form' : form }
	return render(request, 'adminpanel/resource/resource_form.html',context)

def updateResource(request, pk):
	
	resource = Resource.objects.get(id = pk)
	form = ResourceForm(instance =resource);
	if request.method == 'POST':
		form = ResourceForm(request.POST, instance = resource)
		if form.is_valid():
			form.save()
			return redirect('prepare')


	context = {'form' : form , 'item' : resource}
	return render(request, 'adminpanel/resource/update_resource.html',context)	

def deleteResource(request, pk):
	
	resource = Resource.objects.get(id = pk)
	if request.method == 'POST':
		resource.delete()
		return redirect('prepare')

	context = {'item' : resource}
	return render(request, 'adminpanel/resource/delete_resource.html',context)	



def createStudent(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('deadline')
       	 
	context = {'form' : form }
	return render(request, 'adminpanel/student_form.html',context)

def updateStudent(request, pk):
	
	st = Student.objects.get(id = pk)
	form = StudentForm(instance =st);
	if request.method == 'POST':
		form = StudentForm(request.POST, instance = st)
		if form.is_valid():
			form.save()
			return redirect('deadline')


	context = {'form' : form , 'item' : st}
	return render(request, 'adminpanel/update_student.html',context)	

def deleteStudent(request, pk):
	
	st = Student.objects.get(id = pk)
	if request.method == 'POST':
		st.delete()
		return redirect('deadline')

	context = {'item' : st}
	return render(request, 'adminpanel/delete_student.html',context)	


def createSubject(request):
	form = SubjectForm()
	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('deadline')
       	 
	context = {'form' : form }
	return render(request, 'adminpanel/subject_form.html',context)

def updateSubject(request, pk):
	
	st = Subject.objects.get(id = pk)
	form = SubjectForm(instance =st);
	if request.method == 'POST':
		form = SubjectForm(request.POST, instance = st)
		if form.is_valid():
			form.save()
			return redirect('deadline')


	context = {'form' : form , 'item' : st}
	return render(request, 'adminpanel/update_subject.html',context)	

def deleteSubject(request, pk):
	
	st = Subject.objects.get(id = pk)
	if request.method == 'POST':
		st.delete()
		return redirect('deadline')

	context = {'item' : st}
	return render(request, 'adminpanel/delete_subject.html',context)	



def show_club(request , club_id):
	club = Club.objects.get(pk = club_id)
	return render(request, 'clubs/debate.html',{"club": club})

def show_subject(request , course_id):
	course = Course.objects.get(pk = course_id)
	resources1 = course.resources.all().filter(status = "Textbooks")
	resources2 = course.resources.all().filter(status = "Math Forums")
	resources3 = course.resources.all().filter(status = "Online Courses")
	resources4 = course.resources.all().filter(status = "Websites and Blogs")
	resources5 = course.videoresources.all().filter(status = "YouTube Channels")
	resources6 = course.videoresources.all().filter(status = "MIT OpenCourseWare")
	context = {"course": course,"resources2" : resources2,"resources1" : resources1,
	"resources3" : resources3,"resources4" : resources4 ,"resources5" : resources5 ,"resources6" : resources6}

	return render(request, 'subjects/subject1.html',context)

def prepare(request):
	courses = Course.objects.all()
	resources = Resource.objects.all()
	videoresources = Videoresource.objects.all()
	context = {"course_list": courses, "resource_list": resources , "videoresource_list": videoresources}
	if request.user.is_superuser: 
		return render(request, 'adminpanel/editcourse.html',context)	
	else:
		return render(request, 'prepare.html',{ "course_list": courses})

def editcourses(request):
	return render(request, 'adminpanel/editcourse.html',{})	
	


@login_required(login_url ='login')
def deadline(request):
	if request.user.is_superuser: 
		students = Student.objects.all()
		subjects = Subject.objects.all()
		context = {'students' : students, 'subjects' : subjects}
		return render(request, 'adminpanel/editstudent.html',context)
	else:
		subjects = request.user.student.subject_set.all()
		now = datetime.now()
		for subject in subjects: 
			name = calendar.month_name[subject.TimeRemaining.month]
			subject.Name= name
			
		context = {'subjects' : subjects,
					'now' : now}	

		return render(request, 'deadline.html',context )
	

def editstudent(request):
	return render(request, 'adminpanel/editstudent.html',{})	
	
	

def calculator(request):
	return render(request, 'calculator.html',{})

def finalCalculator(request):
	return render(request, 'finalCalculator.html',{})


def scaleTable(request):
	return render(request, 'scaleTable.html',{})

def firstclub(request):
	return render(request, 'clubs/fclub.html',{})

def firstsubject(request):
	return render(request, 'subjects/subject1.html',{})

def debate(request):
	clubs = Club.objects.all()
	return render(request, 'clubs/debate.html',{"club_list": clubs})


def secondcourse(request):
	return render(request, '123courses/2course.html',{})


def thirdcourse(request):
	return render(request, '123courses/3course.html',{})

def faqpage(request):
	return render(request, 'faq.html',{})
