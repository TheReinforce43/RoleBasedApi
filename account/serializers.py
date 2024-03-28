from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','email','password','role' ]
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            return user
        except Exception as exception:
            raise serializers.ValidationError("An error occurred while creating the user: {}".format(str(exception)))