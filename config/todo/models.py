from django.db import models
from django.urls import reverse
# Create your models here.
class Todolist(models.Model):

	title = models.CharField(max_length=200 ,null=False, blank=False, verbose_name="عنوان")
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False, verbose_name="وضعیت" )
	priority = models.CharField(max_length=10, default= 1,  verbose_name="اولویت")

	class Meta:
		ordering = ('-created',)

 
	def __str__(self):
		return self.title

