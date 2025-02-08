from tkinter.font import names

from django.urls import path,include

from weblog.api.v1.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView
from weblog.views import IndexView

urlpatterns = [
    path('home',IndexView.as_view(),name='home'),
    path('create/', ArticleListCreateView.as_view(), name='create'),
    path('retrieve/<int:pk>', ArticleRetrieveUpdateDestroyView.as_view(), name='retrieve'),

]
