from rest_framework import serializers

from .models import FarmOperationType, FarmOperation

class FarmOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmOperation

        fields = [
            'operation_type', 'title', 'details',
            'start_time', 'end_time',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',



class FarmOperationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmOperationType

        fields = [
            'name', 'description',
            'background_color', 'border_color', 'text_color',
        ]
        # 'status', 'created_at', 'updated_at', 'deleted_at',


