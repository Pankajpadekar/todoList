from django.shortcuts import render, get_object_or_404 , redirect
from myapp.models import Task

# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == "POST":
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title , desc)
        ins = Task(task_Title = title , task_Desc = desc)
        ins.save()
        context = {'success' : True}


    return render(request, 'index.html' , context)

def tasks(request):
    all_Tasks = Task.objects.all()
    context = {'tasks': all_Tasks}
    return render(request, 'tasks.html' , context)

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_Title = request.POST['title']
        task_Desc = request.POST['desc']
        task_status = request.POST.get('status') == 'active' # Assuming you have a dropdown with options 'active' and 'inactive
        task.save()
        return redirect('tasks')
    return render(request, 'edit_task.html' , {'task' : task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks')













    # Handle item deletion
    item.delete()
    return redirect()
