from django.shortcuts import render, redirect
from .models import Todo
from .forms import NewTodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo_list = Todo.objects.order_by('-id')

    new_todo_form = NewTodoForm()

    context= {'todo_list':todo_list, 'form':new_todo_form}

    return  render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    new_todo_form = NewTodoForm(request.POST)

    if new_todo_form.is_valid():
        new_todo = new_todo_form.save()

    return redirect('index')


def  completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete= True
    todo.save()

    return redirect('index')


def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')