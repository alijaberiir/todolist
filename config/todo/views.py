
from .models import Todolist
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import  reverse_lazy

class listtodo(ListView):
	queryset = Todolist.objects.all()
	template_name = 'todo/index.html'

class addtodo(CreateView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = '__all__'
	success_url = reverse_lazy("index")


class deltodo(DeleteView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = '__all__'
	success_url = reverse_lazy("index")


class uptodo(UpdateView):
	model = Todolist
	template_name = 'todo/index.html'
	fields = ('status',)
	success_url = reverse_lazy("index")

