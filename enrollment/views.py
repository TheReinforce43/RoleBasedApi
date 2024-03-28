from django.shortcuts import render
from .serializers import EnrollmentSerializer
from .models import EnrollmentModel
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.authtoken.views import APIView
from account.permissions import IsStudent


# class enrollmentApiView(APIView):
#     def post(self,request):
#         serializer=EnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request):
#         enrollment=EnrollmentModel()
#         serializer=EnrollmentSerializer(enrollment)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    

class GetCreateViewAPI(generics.ListCreateAPIView):
    serializer_class=EnrollmentSerializer
    queryset=EnrollmentModel.objects.all()
    permission_classes=[IsStudent]

    

