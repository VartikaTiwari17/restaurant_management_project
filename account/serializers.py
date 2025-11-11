from rest_framework import serializers
from .models import FavoriteMenuItem

class FavoriteMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMenuItem
        fields = ['id', 'menu_item']
