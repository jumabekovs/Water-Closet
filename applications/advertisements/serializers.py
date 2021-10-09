from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class AdvertisementsHistory(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['history'] = AdvertisementSerializer(instance.seller).data
    #     return representation