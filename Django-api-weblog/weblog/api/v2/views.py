from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from weblog.api.v2 import serializers
from weblog.models import Article, Category


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

