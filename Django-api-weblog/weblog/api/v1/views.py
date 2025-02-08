from rest_framework import generics

from weblog.api.v1.serializers import ArticleSerializer
from weblog.models import Article


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer
