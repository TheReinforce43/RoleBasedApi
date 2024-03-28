from rest_framework import serializers
from .models import TeacherModel
from account.models import User
from account.serializers import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model=TeacherModel
        fields='__all__'

    def create(self,validated_data):
        user_data=validated_data.pop('user',None)

        if user_data is None:
            raise serializers.ValidationError('Base User data is required to create a teacher')
        try:
            user_instance=User.objects.create_user(**user_data)
        except Exception as e:
            raise serializers.ValidationError('Errors creating user : {}',format(str(e)))
        teacher=TeacherModel.objects.create(user=user_instance,**validated_data)
      
        return teacher
            


