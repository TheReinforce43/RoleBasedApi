from .models import StudentModel
from account.models  import User
from account.serializers import UserSerializer
from rest_framework import  serializers

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentModel
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None) 

        if user_data is None:
            raise serializers.ValidationError("User data is required to create a student")
        try:
            user_instance = User.objects.create_user(**user_data)
        except Exception as e:
            raise serializers.ValidationError("Error creating user: {}".format(str(e)))
        student = StudentModel.objects.create(user=user_instance, **validated_data)
        return student
