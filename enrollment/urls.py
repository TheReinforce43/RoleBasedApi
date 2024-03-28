from django.urls import path 
from . import views 

urlpatterns = [
    path('add/',views.GetCreateViewAPI.as_view(),name='enrolling'),

]
