from rest_framework import serializers

from farmactivities.models import ActivityType, Activity

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity

        fields = [
            'activity_type', 'title', 'details',
            'start_time', 'end_time',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',



class ActivityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


