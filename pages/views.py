from django.shortcuts import render
from django.http import HttpResponse
from pages.models import TodoTask
from django.shortcuts import redirect

# Create your views here.

def index(request):
    tasks = TodoTask.objects.all()
    return render(request, 'pages/index.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'POST':
        text = request.POST.get('task_text')
        task = TodoTask(text=text)
        task.save()
        return redirect('index')
    tasks = TodoTask.objects.all()
    return render(request, 'pages/index.html', {'tasks': tasks})

