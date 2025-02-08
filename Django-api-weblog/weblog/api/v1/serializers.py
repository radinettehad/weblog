from rest_framework import serializers
from weblog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    serializers.ReadOnlyField(source='Category.name', read_only=True)
    serializers.ReadOnlyField(source='Article.title', read_only=True)

    class Meta:

        model = Article

        fields = '__all__'