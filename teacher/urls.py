from django.urls import path 
from . import views 

urlpatterns = [
    path('signup/',views.TeacherSignUpView.as_view(),name='TeacherSignUpView'),
    path('login/',views.TeacherLoginView.as_view(),name='TeacherloginView'),
]
