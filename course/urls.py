from django.urls import path 
from . import views 

urlpatterns = [
    path('add/',views.CourseCreateDisplayAPI.as_view(),name='add'),
    path('get/',views.CourseCreateDisplayAPI.as_view(),name='get'),
    path('update/<int:pk>',views.CourseUpdateViewAPI.as_view(),name='update'),
    path('single_get/<int:pk>',views.CourseUpdateViewAPI.as_view(),name='single_get'),
    path('delete/<int:pk>',views.CourseDeleteViewAPI.as_view(),name='delete'),
]
