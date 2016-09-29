from . import models
from . import serializers
from .forms import PostForm
from django.forms import widgets
from django.shortcuts import render
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_extensions import mixins

# Create your views here.

class PostViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    custom_serializer_classes = {
        'retrieve': serializers.PostDetailSerializer,
    }
    pagination_class = PageNumberPagination

class TagViewSet(mixins.NestedViewSetMixin, CustomSerializerViewSet, viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    custom_serializer_classes = {
        'retrieve': serializers.TagDetailSerializer,
    }

class PostSchemaViewSet(viewsets.ViewSet):
    def list(self, request):
        def schema_for(field):
            if isinstance(field.widget, widgets.TextInput):
                return dict(
                    type='text',
                )
            elif isinstance(field.widget, widgets.Textarea):
                return dict(
                    type='textArea',
                    rows=int(field.widget.attrs['rows']),
                )
            elif isinstance(field.widget, widgets.CheckboxInput):
                return dict(
                    type='checkbox',
                )
            else:
                return dict(
                    type='text',
                    placeholder='Unknown ' + repr(field.widget),
                )

        return Response({
            'schema': {
                'fields': [
                    schema_for(field)
                    for name, field in PostForm().fields.items()
                ],
            },
        })
