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

def edit_view(request, pk):
    item = get_object_or_404(Task, pk=pk)
    # Handle form submission for editing the item
    return render(request , '')











    # Handle item deletion
    item.delete()
    return redirect()
