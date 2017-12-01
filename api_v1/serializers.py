from rest_framework import serializers
from .models import Data_ingest_line
from django.utils import timezone



class Data_ingest_lineSerializer(serializers.Serializer):
    channel_id = serializers.CharField(max_length=50,default="none")
    #value  = serializers.FloatField()
    timestamp = serializers.DateTimeField(default=timezone.now)
    concentration = serializers.FloatField()
    morphology = serializers.FloatField()
    motility = serializers.FloatField()
    weight = serializers.FloatField()
    height = serializers.FloatField()
    bmi = serializers.FloatField()
    std = serializers.IntegerField(max_value=1, min_value=0)
    smoker = serializers.IntegerField(max_value=1, min_value=0)
    exercise = serializers.IntegerField(max_value=1, min_value=0)
    
    conceive = serializers.IntegerField(max_value=1, min_value=0)
    
   
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Data_ingest_line.objects.create(**validated_data)

class Data_ingest_bulkSerializer(serializers.Serializer):
    datapoints = Data_ingest_lineSerializer(many=True)
    upload_ref_ID = serializers.CharField(max_length=50)
    #content = serializers.CharField(max_length=200)
    #created = serializers.DateTimeField()