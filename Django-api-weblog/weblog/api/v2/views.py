from django.contrib.sites import requests
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from weblog.api.v2 import serializers
from weblog.models import Article, Category
from django.views import View


class list(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        listofall = Article.objects.all()
        serializer = serializers.ArticleSerializer(listofall, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class listmodelsview(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class categorymodellist(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.categorySerializer

class listallofcategoriesarticlemodelview(viewsets.ModelViewSet):

    queryset = Category.objects.prefetch_related('articles').filter(pk=2)
    serializer_class = serializers.categorySerializer

class ArticleViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Article.objects.all()
        serializer = serializers.ArticleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            queryset = Article.objects.get(pk=pk)
            serializer = serializers.ArticleSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            raise NotFound("Article not found.")

    def put (self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = serializers.ArticleSerializer(article, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            raise NotFound("Article not found.")

    def patch (self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = serializers.ArticleSerializer(article, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            raise NotFound("Article not found.")

    def delete (self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            raise NotFound("Article not found.")


# class ArticleDetailView(View):
#     def get(self, request, pk):
#         response = requests.get(f'http://127.0.0.1:8000/api/articles/{pk}/')
#         article = response.json()
#         return render(request, 'article_detail.html', {'article': article})

