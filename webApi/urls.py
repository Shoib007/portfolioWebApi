from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetchAPI),
    path('projects', views.projectsForm),
    path('skills', views.skillsForm),
    path('post', views.saveForm, name='post')
]