from django.urls import path, include
from rest_framework import routers

from applications.advertisements.views import AdvertisementsViewSet#, WatchVideo,

router = routers.DefaultRouter()

router.register('', AdvertisementsViewSet)


urlpatterns = [
    # path('watch-video/', WatchVideo.as_view()),
    path('', include(router.urls))
]
urlpatterns += router.urls