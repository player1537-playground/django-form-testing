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
from collections import OrderedDict
import copy

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

################

class ComponentRegistry(object):
    def __init__(self):
        self.components = dict()

    def add(self, widget_cls, component_cls):
        self.components[widget_cls] = component_cls()

    def lookup(self, field):
        for (widget_cls, component) in self.components.items():
            if isinstance(field.widget, widget_cls):
                return component
        raise KeyError('Could not find component "{!r}"'.format(component))

registry = ComponentRegistry()

def register_schema_for(widget_cls):
    def wrapper(component_cls):
        registry.add(widget_cls, component_cls)
        return component_cls
    return wrapper

class DeclarativeFieldsMetaclass(type):
    """
    Metaclass that collects Fields declared on the base classes.
    """
    def __new__(mcs, name, bases, attrs):
        current_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                current_fields.append((key, value))
                attrs.pop(key)

        attrs['declared_fields'] = OrderedDict(current_fields)

        new_class = super().__new__(mcs, name, bases, attrs)

        # Walk through the MRO.
        declared_fields = OrderedDict()
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, 'declared_fields'):
                declared_fields.update(base.declared_fields)

            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in declared_fields:
                    declared_fields.pop(attr)

        new_class.base_fields = declared_fields
        new_class.declared_fields = declared_fields
        new_class.attrs = declared_fields

        return new_class

class Schema(object):
    """
    A schema takes in a form and returns a dictionary representing the fields
    in it.
    """
    def render(self, form_cls):
        return dict(
            schema=dict(
                fields=[
                    registry.lookup(field).render(field)
                    for (name, field) in form_cls().fields.items()
                ],
            ),
        )

class Component(object):
    def __init__(self, attrs=None):
        if attrs is None and self.attrs is None:
            self.attrs = dict()
        elif attrs is not None and self.attrs is not None:
            self.attrs.update(attrs)
        else:
            pass  # Don't need to do anything

    def render(self, field, attrs=None):
        if attrs is None:
            attrs = dict()

        d = dict()

        for (key, value) in self.attrs.items():
            d[key] = value.render(field=field)

        for (key, value) in attrs:
            d[key] = value.render(field=field)

        return d

class Field(object):
    def render(self, field):
        raise NotImplementedError('Field.render needs to be defined')

class Attr(Field):
    def __init__(self, attr, default=None, type=None):
        self.attr = attr
        self.default = default
        if type is None:
            self.type = lambda x: x
        else:
            self.type = type

    def render(self, field):
        try:
            x = field
            for attr in self.attr.split('.'):
                x = getattr(x, attr)
            return self.type(x)
        except AttributeError:
            return self.default

class Name(Field):
    def render(self, field):
        return field.label

class Func(Field):
    def __init__(self, func):
        self.func = func

    def render(self, field):
        return self.func(field)

class Literal(Field):
    def __init__(self, value):
        self.value = value

    def render(self, *args, **kwargs):
        return self.value

class BaseComponent(Component, metaclass=DeclarativeFieldsMetaclass):
    label = Attr('label')
    hint = Attr('help_text')
    model = Name()
    default = Attr('default', default=None)
    required = Attr('required')

@register_schema_for(widgets.TextInput)
class TextComponent(BaseComponent, metaclass=DeclarativeFieldsMetaclass):
    type = Literal('text')

@register_schema_for(widgets.Textarea)
class TextAreaComponent(BaseComponent, metaclass=DeclarativeFieldsMetaclass):
    type = Literal('textArea')
    rows = Func(lambda field: int(field.widget.attrs['rows']))

@register_schema_for(widgets.CheckboxInput)
class CheckboxComponent(BaseComponent, metaclass=DeclarativeFieldsMetaclass):
    type = Literal('checkbox')

################

class PostSchemaViewSet(viewsets.ViewSet):
    def list(self, request):
        schema = Schema()
        return Response(schema.render(PostForm))
