from rest_framework import serializers
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = CustomUser
		fields = '__all__'
		extra_kwargs = {
			'password': {'write_only':True},
		}

	def create(self, validated_data):
		del validated_data['password2']
		return CustomUser.UserManagers.create_user(**validated_data)
			
	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('passwords must match')
		return data


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'
