from . import models
from . import serializers
from .forms import PostForm
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_extensions import mixins
from django_vueformgenerator.schema import Schema


class PostViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    custom_serializer_classes = {
        'retrieve': serializers.PostDetailSerializer,
    }
    pagination_class = PageNumberPagination


class TagViewSet(mixins.NestedViewSetMixin, CustomSerializerViewSet,
                 viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    custom_serializer_classes = {
        'retrieve': serializers.TagDetailSerializer,
    }


class PostSchemaViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(Schema().render(PostForm))
