from django.urls import path 
from . import views 


urlpatterns = [
    path('signup/',views.StudentSignupView.as_view(),name='signup'),
    path('login/',views.StudentLoginView.as_view(),name='login'),
]
