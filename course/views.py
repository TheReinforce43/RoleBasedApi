from django.shortcuts import render
from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework import generics,mixins
from rest_framework.permissions import IsAdminUser
from account.permissions import IsAdminOrTeacher


class CourseCreateDisplayAPI(generics.ListCreateAPIView):
    serializer_class=CourseSerializer
    queryset=CourseModel.objects.all()
    permission_classes=[IsAdminOrTeacher]


class CourseUpdateViewAPI(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset=CourseModel.objects.all()
    permission_classes=[IsAdminOrTeacher]

    def get(self,request,pk):
        return self.retrieve(request)   #Here only one item is returned
    
    def put(self,request,pk):
        return self.update(request)


class CourseDeleteViewAPI(mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class=CourseSerializer
    queryset=CourseModel.objects.all()
    Permission_classes=[IsAdminUser]   

    def delete(self,request,pk):
        return self.destroy(request)                 