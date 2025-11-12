from account import serializers
from orders.models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name', 'max_capacity']  # ✅ Added max_capacity
