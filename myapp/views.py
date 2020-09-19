from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Author, Post, Language
from .serializers import LanguageSerializer, AuthorSerializer, PostSerializer
# Create your views here.


class AuthorPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })


class AuthorView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    queryset = Author.objects.all()

    # def get_queryset(self):
    #     return self.queryset.filter(location__icontains="Pakistan")


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['created_by'] = instance.get_author_location()
        return Response(data)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        author = Author.objects.get(id=1)
        serializer.save(author=author)


class LanguageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Language.objects.all()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LanguageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(instance=queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(instance=queryset)
        queryset.delete()
        return Response(serializer.data)


class AuthorViewSet(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # def perform_create(self, serializer):
    #     serializer.save()

    # def create(self, request):
    #     serializer = AuthorSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
