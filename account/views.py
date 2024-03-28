from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import status,mixins,generics
from rest_framework.response import Response
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.views  import ObtainAuthToken,APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class UserSignUp(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class UserLogin(ObtainAuthToken):
    def post(self, request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            if created:
                token.delete()
                token=Token.objects.create(user=user)

            return Response(
                {
                    'token':token.key,
                    'username':user.username,
                    'role':user.role
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({'message':"Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
class UserLogout(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        print(request.headers)
        token_key=request.auth.key 
        token=Token.objects.get(key=token_key)
        token.delete()

        return Response({'message':"User Logout Sueccessfully"})




