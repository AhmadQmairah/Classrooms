from django import forms
from .models import Classroom,Student	
from django.contrib.auth.models import User
class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        
        exclude=['Teacher']


class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets={"password":forms.PasswordInput()}


class LogInForm(forms.Form	):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
        
 
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude=['classroom']	
 

		

		

        