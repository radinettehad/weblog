from django.urls import path, include
from rest_framework.routers import DefaultRouter


from weblog.api.v2.views import listmodelsview, categorymodellist, listallofcategoriesarticlemodelview, ArticleViewSet \


router = DefaultRouter()
router.register('listmodel',listmodelsview,basename='listmodel' )
router.register('categorylist',categorymodellist,basename='categorylist' )
router.register('categoryalltitle',listallofcategoriesarticlemodelview,basename='categoryalltitle' )
router.register('articleViewSet',ArticleViewSet,basename='articleViewSet' )

urlpatterns = [
    path ('',include(router.urls)),
    # path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # path('articleViewSet/',articleViewSet.as_view(),name='articleViewSet'),

]