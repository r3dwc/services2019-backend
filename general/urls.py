from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from . import views

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Service2019 API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'merchants', views.MerchantViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)