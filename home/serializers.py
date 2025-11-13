from rest_framework import serializers # type: ignore
from django.utils import timezone # type: ignore
from datetime import timedelta
from .models import DailySpecial


class DailySpecialSerializer(serializers.ModelSerializer):
    time_remaining = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DailySpecial
        fields = '__all__'  # or list fields manually if preferred
        read_only_fields = ('time_remaining',)

    def get_time_remaining(self, obj):
        # Ensure the model has an 'end_time' field
        if not hasattr(obj, 'end_time') or obj.end_time is None:
            return "No expiration time set"

        now = timezone.now()
        if obj.end_time < now:
            return "Expired"

        # Calculate time difference
        remaining = obj.end_time - now
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        days = remaining.days

        # Format output
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

        return ", ".join(parts) if parts else "Less than a minute"
