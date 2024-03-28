from django.shortcuts import render
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.authtoken.views import APIView 

from .models import CategoryModel
from .serializers import CategorySerializer
from account.permissions import IsTeacher


# class categoryapiview(APIView):
#     permission_classes=[IsAdminUser]

#     def post(self,request):
#         serializer=CategorySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class categoryapiviewNonKey(generics.ListCreateAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]

class categoryapiviewKey(generics.RetrieveUpdateDestroyAPIView):
    queryset=CategoryModel.objects.all
    serializer_class=CategorySerializer
    permission_classes=[IsAdminUser]

