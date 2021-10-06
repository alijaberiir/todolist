from django.shortcuts import render,HttpResponseRedirect
from .models import Todolist
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


class listtodo(ListView):
	queryset = Todolist.objects.all()
	template_name = 'todo/index.html'

class addtodo(CreateView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = '__all__'
	success_url = ('/')


class deltodo(DeleteView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = '__all__'
	success_url = ('/')


class uptodo(UpdateView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = ('status',)
	success_url = ('/')

