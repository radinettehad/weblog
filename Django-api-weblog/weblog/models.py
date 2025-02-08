from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="article")

    title = models.CharField(max_length=200)

    content = models.TextField()

    author = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)



    def __str__(self):

        return self.title
