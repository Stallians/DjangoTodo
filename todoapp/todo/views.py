from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Task


def alltasks(request):
    open_tasks = Task.objects.filter(is_complete=False)
    closed_tasks = Task.objects.filter(is_complete=True)
    context = {
        "open_tasks": open_tasks,
        "closed_tasks": closed_tasks,
    }
    return render(request, "todo/index.html", context)


def add(request):
    if request.method == "GET":
        return render(request, "todo/add.html")
    elif request.method == "POST":
        description = request.POST["task"]
        new_task = Task(description=description)
        new_task.save()
        return HttpResponseRedirect(reverse("alltasks"))


def edit(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    if request.method == "GET":
        return render(request, "todo/edit.html", {"task": task})
    elif request.method == "POST":
        task.description = request.POST["description"]
        task.is_complete = request.POST["is_complete"]
        task.save()
        return HttpResponseRedirect(reverse("alltasks"))


def toggle_status(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    task.is_complete = not (task.is_complete)
    task.save()
    return HttpResponseRedirect(reverse("alltasks"))


def delete(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    task.delete()
    return HttpResponseRedirect(reverse("alltasks"))
