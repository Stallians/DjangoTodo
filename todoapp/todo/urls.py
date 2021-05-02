from django.urls import path

from . import views

urlpatterns = [
    path("", views.alltasks, name="alltasks"),
    path("add/", views.add, name="add_task"),
    path("toggle/<int:taskid>", views.toggle_status, name="toggle_status"),
    path("delete/<int:taskid>", views.delete, name="delete_task"),
    path("edit/<int:taskid>", views.edit, name="edit_task"),
]
