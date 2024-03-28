from django.urls import path 
from . import views 

urlpatterns = [
    path('add/',views.categoryapiviewNonKey.as_view(),name='category'),
    path('add/<int:pk>',views.categoryapiviewKey.as_view(),name='category'),
]
