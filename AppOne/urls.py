from django.urls import path, include

from .views import ArticleAPIView, ArticleDetails, ArticleGenericApiView, ArticleDetailsGenericApiView, ArticlesViewSet, ArticlesGenericViewSet, ArticlesModelViewSet
from rest_framework import routers
#
router = routers.DefaultRouter()
router.register('articles', ArticlesViewSet, basename="article")

router2 = routers.DefaultRouter()
router2.register('articles', ArticlesGenericViewSet, basename="article")

router3 = routers.DefaultRouter()
router3.register('articles', ArticlesModelViewSet, basename="article")

# router.register(r'articles/<str:id>/', ArticleDetails.as_view(), basename="articles-details")

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<str:pk>/', article_detail)
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<str:id>/', ArticleDetails.as_view()),

    path('generic/articles/', ArticleGenericApiView.as_view()),
    path('generic/articles/<str:id>/', ArticleDetailsGenericApiView.as_view()),
    path('viewset/', include(router.urls)),
    path('genericViewset/', include(router2.urls)),
    path('modelViewset/', include(router3.urls))
]

# urlpatterns += router.urls
