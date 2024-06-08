from rest_framework.routers import DefaultRouter

from geo_service.views import QueryLogViewset


router = DefaultRouter()
router.register(r'query', QueryLogViewset, basename='query')
urlpatterns = router.urls