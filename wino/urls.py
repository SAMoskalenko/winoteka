from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'country', CountryViewSet, basename='country')
router.register(r'region', RegionViewSet, basename='region')
router.register(r'area', AreaViewSet, basename='area')
router.register(r'quality', QualityViewSet, basename='quality')
router.register(r'drink', DrinkViewSet, basename='drink')

urlpatterns = router.urls
