from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    counting = Todo.objects.count()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    context = {'todos':todos, 'counting':counting, 'form':form}
    return render(request, "todo/index.html", context)

def detail(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {'todo':todo}
    return render(request, "todo/detail.html", context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
    context = {'form':form}
    return render(request, "todo/edit.html", context)