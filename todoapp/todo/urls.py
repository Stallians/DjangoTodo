from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet)


urlpatterns = [
    path("", views.alltasks, name="alltasks"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("add/", views.add, name="add_task"),
    path("toggle/<int:taskid>", views.toggle_status, name="toggle_status"),
    path("delete/<int:taskid>", views.delete, name="delete_task"),
    path("edit/<int:taskid>", views.edit, name="edit_task"),
]
