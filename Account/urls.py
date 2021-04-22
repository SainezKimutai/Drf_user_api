
from rest_framework import routers

from .views import AuthViewSet, UsersViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UsersViewSet, basename='user')
router.register('auth', AuthViewSet, basename='authentication')

urlpatterns = router.urls
