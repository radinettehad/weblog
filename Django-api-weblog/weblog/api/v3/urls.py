from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('prrrrro', modelViewSet, basename='proo')
router.register('categoryyyy', modelModelViewSet, basename='categoooory')
# urlpatterns = router.urls
# urlpatterns += [

urlpatterns = [
    path('', include(router.urls)),
    path('pro_list/', modelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }
    ) , name='pro_list_create'),

    path('pro_detail/<int:id>/', modelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
    ) , name='pro_detail'),
    # path('product/list/<int:id>', ProductListDetailAPIView.as_view() , name='pro_list_create'),
]
