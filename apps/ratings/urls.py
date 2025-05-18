from rest_framework.routers import DefaultRouter
from .views import BookRatingViewSet

router = DefaultRouter()
router.register(r'', BookRatingViewSet, basename='ratings')

urlpatterns = router.urls