from .models import Prediction
from rest_framework import serializers


class PredictionSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            'text': obj.text,
            'class': obj.class_ind
        }

    class Meta:
        model = Prediction
        fields = ('text', 'class_ind')
