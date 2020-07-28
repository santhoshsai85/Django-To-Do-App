from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.utils import timezone
# Create your views here.
def index(request):
	todo_items=Task.objects.all().order_by("-added_date")

	return render(request,'tasks/list.html',{"todo_items":todo_items})


@csrf_exempt
def add_todo(request):
	current_date=timezone.now()
	content=request.POST["content"]
	Task.objects.create(added_date=current_date,text=content)
	return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request,todo_id):
	Task.objects.get(id=todo_id).delete()
	return HttpResponseRedirect("/")