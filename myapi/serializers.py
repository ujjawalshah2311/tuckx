from rest_framework import serializers
from .models import dashcamvideo,dashcam

class dashcamvideoSerializer(serializers.ModelSerializer):

    class Meta:
        model =  dashcamvideo
        fields = '_all_'

class dashcamSerializer(serializers.ModelSerializer):

    class Meta:
        model =  dashcam
        fields = '_all_'