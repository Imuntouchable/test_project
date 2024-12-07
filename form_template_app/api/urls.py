from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FormValidationViewSet

router = DefaultRouter()
router.register(
    r'get_form',
    FormValidationViewSet,
    basename='get_form'
)

urlpatterns = [
    path('', include(router.urls)),
]
