from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
from .yasg import urlpatterns as url_doc

router = DefaultRouter()
router.register('work', views.WorkViewSet)
router.register('category', views.CategoryViewSet)
router.register('skills', views.SkillsViewSet)
router.register('country', views.CountryViewSet)
router.register('city', views.CityViewSet)
router.register('address', views.AddressViewSet)

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('', include(router.urls))
]

urlpatterns += url_doc
