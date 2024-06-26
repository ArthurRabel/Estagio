import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    task_list = Task.objects.all()
    context = {"task_list": task_list}
    return render(request, "polls/index.html", context)

def edit(request, task_id):
    if request.method == 'POST':
        task_selected = Task.objects.get(pk=task_id)
        context = {"task_selected": task_selected}  
        return render(request, "polls/taskEdit.html", context)

def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        Task.objects.create(title_task=title,text_task=text)
        return redirect('index')
    
def delete(request, task_id):
    if request.method == 'DELETE':
        Task.objects.get(pk=task_id).delete()
    
def put(request, task_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        task = Task.objects.get(pk=task_id)
        task.title_task = data['title']
        task.text_task = data['text']
        task.save()