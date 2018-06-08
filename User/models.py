import sys
try:
    from django.db import models
    from django.contrib.postgres.fields import JSONField
    from rest_framework import serializers
    " https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/#jsonfield "
except Exception as e:
    print("There was an error loading django modules. Do you have django installed?", e)
    sys.exit()


# Sample User model
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    registered = models.DateTimeField(auto_now_add=True)
    settings = JSONField()
    created_by = models.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
