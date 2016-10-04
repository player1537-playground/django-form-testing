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

cache = {}

def register_schema_for(widget_cls):
    def wrapper(func):
        cache[widget_cls] = func
        return func
    return wrapper

def schema_for(form_cls):
    def lookup(field):
        for (widget_cls, func) in cache.items():
            if isinstance(field.widget, widget_cls):
                return func

    form = form_cls()

    return dict(
        schema=dict(
            fields=[
                lookup(field)(name, field)
                for name, field in form.fields.items()
            ],
        ),
    )

def base_schema(name, field, **kwargs):
    return dict(
        label=field.label,
        hint=field.help_text,
        model=name,
        default=getattr(field, 'default', None),
        required=field.required,
        **kwargs,
    )

@register_schema_for(widgets.TextInput)
def schema_for_text_input(name, field):
    return base_schema(
        name,
        field,
        type='text',
    )

@register_schema_for(widgets.Textarea)
def schema_for_textarea(name, field):
    return base_schema(
        name,
        field,
        type='textArea',
        rows=int(field.widget.attrs['rows']),
    )

@register_schema_for(widgets.CheckboxInput)
def schema_for_checkbox_input(name, field):
    return base_schema(
        name,
        field,
        type='checkbox',
    )

class PostSchemaViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(schema_for(PostForm))
