from rest_framework import serializers
from weblog.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        # read_only_fields = ('id','title','author','published')

        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):
    articles=ArticleSerializer(many=True,read_only=True)
    class Meta:

        model = Category
        fields = ['id','name','articles']

