from django.db import models
from django.urls import reverse
from django.contrib.auth.models		import User	
class Classroom(models.Model):
	
    

	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	Teacher=models.ForeignKey(User,on_delete=models.CASCADE	)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	Genders = [
    ('male', 'male'),
    ('female', 'female	')]

	name = models.CharField(max_length=120)
	date_of_birth=models.DateField(	)
	gender=models.CharField(max_length=120,choices=Genders)
	exam_grade=models.DecimalField(max_digits=5,decimal_places=3)
	classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE	,)


	