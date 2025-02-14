from tkinter.font import names

from django.urls import path,include

from weblog.api.v1.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView
from weblog.api.v2.views import list
from weblog.views import IndexView

urlpatterns = [
    path('home',IndexView.as_view(),name='home'),
    path('api/',include('weblog.api.v1.urls')),
    path('api/',include('weblog.api.v2.urls'),)


#     path('create/', ArticleListCreateView.as_view(), name='create'),
#     path('list/',list.as_view(),name='list'),
#     path('retrieve/<int:pk>', ArticleRetrieveUpdateDestroyView.as_view(), name='retrieve'),
#
]
