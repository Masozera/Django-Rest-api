from django.shortcuts import render
from django.views.generic import ListView,DetailView, View
from .models import Lesson,HomePageFormModel
from .forms import HomePageForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from rest_framework import generics
# from .serializers import LessonSerializer


# Create your views here.
# class HomePageView(ListView):
   
#     model          = Lesson
#     context_object_name = 'lessons'
#     template_name  = "homepage.html"
# TODO HOW to receive post of a form in list View


def HomePage(request):
        lessons = Lesson.objects.all()
        form    = HomePageForm()
        
        if request.method == 'POST':
            form    = HomePageForm(request.POST)
            if form.is_valid():
                email        = form.cleaned_data['email']
                message        = form.cleaned_data['message']
                
            
                entry  = HomePageFormModel()

                entry.email   = email
                entry.message = message
                entry.save()

                return HttpResponseRedirect('/')


        context= { 'form':form}
        return render(request,"homepage.html", context)

# class ListLesson(generics.ListAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonSerializer