from rest_framework import routers

from .apiviews import FreeFairApiView

app_name = 'api_free_fair'

router = routers.DefaultRouter()
router.register(r'v1/api_free_fair', FreeFairApiView, base_name='FreeFair')

urlpatterns = router.urls
