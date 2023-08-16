from django.shortcuts import render,redirect
from first_app.forms import TaskStoreForm
from first_app.models import TaskModel

# Create your views here.



def add_task(request):
    if request.method =='POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('showtask')
    else:
        task = TaskStoreForm()
            
            
    return render(request,'add_task.html',{'form':task})


def show_task(request):
    task = TaskModel.objects.all()
    # print(task)
    return render(request,'show_task.html',{'data': task})

def edit_task(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskStoreForm(instance = task)
    if request.method =='POST':
        task = TaskStoreForm(request.POST,instance=task)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('showtask')
    return render(request,'add_task.html',{'form': form})


def delete_task(request,id):
     task = TaskModel.objects.get(pk = id).delete()
     return redirect('showtask')
def com_task(request, id):
    tasks = TaskModel.objects.get(pk=id)
    tasks.is_completed = True
    task = TaskModel.objects.all()
    tasks.save()
    return render(request, 'com_task.html', {'data':task})

def delete_task_com(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    task = TaskModel.objects.all()
    return render(request, 'com_task.html', {'data':task})
    