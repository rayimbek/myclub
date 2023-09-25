from django import forms
from django.forms import ModelForm, DateTimeInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import * 

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'type' : 'password'}))
	new_password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs = {'class' : 'form-control' , 'type' : 'password'}))
	new_password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs = {'class' : 'form-control' , 'type' : 'password'}))

	class Meta:
		model = User 
		fields = ('old_password' , 'new_password1', 'new_password2')



class ClubForm(ModelForm):
	class Meta:
		model = Club
		fields = '__all__'	


class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = '__all__'		


class VideoResourceForm(ModelForm):
	class Meta:
		model = Videoresource
		fields = '__all__'		


class ResourceForm(ModelForm):
	class Meta:
		model = Resource
		fields = '__all__'		


class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2'] 


class SubjectForm(ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'		
		widgets = {
            'TimeRemaining': DateTimeInput(attrs={'type': 'datetime-local'}),
        }