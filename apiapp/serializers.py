from rest_framework import serializers
from .models import APIData


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=APIData
        fields=('vid_id' ,'vid_title' ,'vid_publishDate' ,'vid_description' ,'logo_url')