from django.urls import path, include
from rest_framework.routers import DefaultRouter


from weblog.api.v2.views import listmodelsview, categorymodellist

router = DefaultRouter()
router.register('listmodel/',listmodelsview,basename='listmodel' )
router.register('categorylist/',categorymodellist,basename='categorylist' )

urlpatterns = [
    path ('',include(router.urls)),

]