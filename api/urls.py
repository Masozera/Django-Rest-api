from .views import ListLesson
from django.urls import path

urlpatterns = [
    # path('', HomePage, name='homepage')
    path('', ListLesson.as_view())
]