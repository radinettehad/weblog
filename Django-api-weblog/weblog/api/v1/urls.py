from django.urls import path,include

from weblog.api.v1.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    # path('create/',ArticleListCreateView.as_view(),name='create'),
    # path('retrieve/',ArticleRetrieveUpdateDestroyView.as_view(),name='retrieve'),



]