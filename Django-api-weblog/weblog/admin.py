from django.contrib import admin
from django.contrib.auth.models import User
from weblog.models import Category, Article

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)