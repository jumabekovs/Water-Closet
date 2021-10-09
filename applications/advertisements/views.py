from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.advertisements.models import Advertisement
from applications.advertisements.permissions import IsOwnerOrAdmin
from applications.advertisements.serializers import AdvertisementSerializer


# class WatchVideo(APIView):
#     random_idx = random.randint(0, Advertisement.objects.filter(is_validated=True).count() - 1)
#     advertisement = Advertisement.objects.all()[random_idx]
#
#     def get(self, request):
#         random_idx = random.randint(0, Advertisement.objects.filter(is_validated=True).count() - 1)
#         advertisement = Advertisement.objects.all()[random_idx]
#         return HttpResponse(advertisement)


class AdvertisementsViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    search_fields = ['title', ]
    ordering_fields = ['is_validated', ]
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes = [IsOwnerOrAdmin, ]
        return super().get_permissions()


