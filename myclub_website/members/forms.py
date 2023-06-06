from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'type' : 'password', 'style': 'width: 350px;'}))
	new_password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs = {'class' : 'form-control' , 'type' : 'password', 'style': 'width: 350px;'}))
	new_password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs = {'class' : 'form-control' , 'type' : 'password', 'style': 'width: 350px;'}))

	class Meta:
		model = User 
		fields = ('old_password' , 'new_password1', 'new_password2')