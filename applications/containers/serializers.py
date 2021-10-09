from rest_framework import serializers
from .models import Toilet


class ToiletSerializers(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = '__all__'