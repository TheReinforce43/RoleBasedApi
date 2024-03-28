from django.urls import path 
from . import views 

urlpatterns = [
    
    path('signup/',views.UserSignUp.as_view(),name='signup'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('logout/',views.UserLogout.as_view(),name='logout'),
]
