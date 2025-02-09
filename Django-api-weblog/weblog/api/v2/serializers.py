from rest_framework import serializers
from weblog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Article

        read_only_fields = ('id','title','author','published')

        fields = '__all__'