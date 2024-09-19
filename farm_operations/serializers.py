from rest_framework import serializers

from .models import FarmActivityType, FarmActivity

class FarmActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmActivity

        fields = [
            'activity_type', 'title', 'details',
            'start_time', 'end_time',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',



class FarmActivityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmActivityType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


