from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import projectDB
from .Serializer import projectSerializer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.

@api_view(['GET'])
def fetchAPI(request):
    projectData = projectDB.objects.all()
    serializedProjectData = projectSerializer(projectData, many=True)
    return Response( serializedProjectData.data )

@api_view(['POST'])
def saveForm(request):
    formData = projectSerializer(data = request.data)
    if formData.is_valid():
        formData.save()
    else:
        return Response({formData.errors})
    return HttpResponse("Data Has been Saved")


def projectsForm(request):
    return render(request, 'projects.html')

def skillsForm(request):
    return render(request, 'skills.html')
