from django.urls import path
from .views import  HomePage

urlpatterns = [
    # path('', HomePageView.as_view(), name='homepage'),
    path('', HomePage, name='homepage')
]