from django.urls import path
from .views import (
    IndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleStatusView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/toggle-status/", TaskToggleStatusView.as_view(), name="task-toggle-status"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]