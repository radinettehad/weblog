from django.urls import path,include

from weblog.api.v1.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView
from weblog.api.v2.views import list

urlpatterns = [
    # path('create/',ArticleListCreateView.as_view(),name='create'),
    # path('retrieve/',ArticleRetrieveUpdateDestroyView.as_view(),name='retrieve'),
    path('create/', ArticleListCreateView.as_view(), name='create'),
    path('list/',list.as_view(),name='list'),
    path('retrieve/<int:pk>', ArticleRetrieveUpdateDestroyView.as_view(), name='retrieve'),

]



