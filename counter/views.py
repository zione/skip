from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import permissions,viewsets,renderers
from rest_framework.decorators import (permission_classes,detail_route)
from rest_framework.response import Response
from rest_framework import filters

from .serializers import PosterSerializer
from .models import Poster

# Create your views here.

class PosterViewSet(viewsets.ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
