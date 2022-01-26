from django.shortcuts import render
from rest_framework import generics
from .serializers import LessonSerializer
from django.views.generic import ListView,DetailView, View
from home_page_app.models import Lesson,HomePageFormModel

# Create your views here.

class ListLesson(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer