from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import *

UserModel = get_user_model()

#create a new user
class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj


#authenticate the username and the password of the user
class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

#return the loggedin user
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('email', 'username')

class ProjetSerializer(serializers.ModelSerializer):
	class Meta:
		model=Projet
		fields='__all__'

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Document
		fields='__all__'


class RevisionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Revision
		fields='__all__'


class AppUserSerializer(serializers.ModelSerializer):
	class Meta:
		model=AppUser
		fields='__all__'