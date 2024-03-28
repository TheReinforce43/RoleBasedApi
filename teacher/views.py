from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from account.serializers import UserSerializer
from .serializers import TeacherSerializer
from .models import TeacherModel
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.views import ObtainAuthToken,APIView



class TeacherSignUpView(APIView):

    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class TeacherLoginView(APIView):

    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)

        if user is None:
            raise ValueError('Invalid username or password')
        else:
            login(request,user)
            token,create=Token.objects.get_or_create(user=user)

            if token:
                token.delete()
            token=Token.objects.create(user=user)
            response_data=(
                {
                    
                    'token':token.key,
                    'username':user.username,
                    'role':user.role
                }
            )
            if user.role=='teacher':
                teacher_instance=user.teacher 

                if teacher_instance is not None:
                    teacher_data=TeacherSerializer(teacher_instance).data
                    response_data['data']=teacher_data

                    return Response(response_data,status=status.HTTP_201_CREATED)
                
                else:
                    return Response({'message':'Teacher is invalid'},status=status.HTTP_400_BAD_REQUEST)
            else:
                raise ValueError('Only Teacher role person can login')    

        