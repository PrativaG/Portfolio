from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('skills', views.skills),
    path('experience', views.experience),
    path('projects', views.projects)
]
