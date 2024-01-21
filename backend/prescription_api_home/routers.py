from rest_framework.routers import DefaultRouter

from prescriptions.viewsets import PrescriptionGenericViewSet

router = DefaultRouter()
router.register('prescriptions', PrescriptionGenericViewSet, basename='prescriptions')

urlpatterns = router.urls