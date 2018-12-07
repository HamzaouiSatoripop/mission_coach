from rest_framework import serializers

from training.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    class Meta():
        model =Training
        fields =[
            'trainee',
            'coach',
            'name',
            'progress',
            'sport',

        ]