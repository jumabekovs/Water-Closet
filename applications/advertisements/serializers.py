from django.core.mail import send_mail
from rest_framework import serializers
from .models import Advertisement
from django.contrib.auth import get_user_model

User = get_user_model()


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        add = Advertisement.objects.create(user=user)
        add.save()
        admins_email = list(User.objects.filter(is_staff=True).values_list('email', flat=True))
        send_mail('Новый заказ',
                  f'Описание: {add}\nПользователь: {user}',
                  "azamatjumma@gmail.com",
                  [user for user in admins_email].append(user.email))
        return add
