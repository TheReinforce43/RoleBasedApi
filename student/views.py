from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views  import APIView,ObtainAuthToken
from account.serializers import UserSerializer
from account.models import User 
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token

class StudentSignupView(APIView):

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class StudentLoginView(ObtainAuthToken):

    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            token,create=Token.objects.get_or_create(user=user)
            if token:
                token.delete() 

            token=Token.objects.create(user=user)
            response_data= ({
            'token':token.key,
            'username':user.username,
            'role':user.role
            })
            if user.role=='student':
                student_instance=user.student

                if student_instance is not None:
                    student_data=StudentSerializer(student_instance).data
                    response_data['data']=student_data
                    return Response(response_data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':"Invalid student Data"},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':"Please login only  student role"},status=status.HTTP_400_BAD_REQUEST) 
               





