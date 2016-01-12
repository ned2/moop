from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import ImageSerializer
from web.models import Image, Collection, Tag


class ImageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
