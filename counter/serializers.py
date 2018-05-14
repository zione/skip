import json

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Poster

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ('title','desc','url','mode','imgurl','publishTime')