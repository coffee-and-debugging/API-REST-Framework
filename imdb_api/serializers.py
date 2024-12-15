from rest_framework import serializers
from .models import *

# class WatchListSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title= serializers.CharField(max_length=50)
#     storyline= serializers.CharField(max_length=100)
#     # platform= serializers.ForeignKey(StreamPlatform, on_delete= serializers.CASCADE)
#     active= serializers.BooleanField(default=True)
#     created= serializers.DateTimeField()
    
#     def create(self, validate_data):
#         return WatchList.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.title= validate_data.get('title', instance.title)
#         instance.storyline= validate_data.get('storyline', instance.storyline)
#         instance.active= validate_data.get('active', instance.active)
#         instance.created= validate_data.get('created', instance.created)
#         instance.save()
#         return instance

class WatchListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= WatchList
        fields= "__all__"
    
    
# class StreamPlatformSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name= serializers.CharField(max_length=50)
#     about= serializers.CharField(max_length=100)
#     website= serializers.URLField(max_length=100)
    
#     def create(self, validate_data):
#         return StreamPlatform.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.name= validate_data.get('name', instance.name)
#         instance.about= validate_data.get('about', instance.about)
#         instance.website= validate_data.get('website', instance.website)
#         instance.save()
#         return instance


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # link= serializers.HyperlinkedIdentityField(view_name ='streamplatform-detail')
    watchlist= WatchListSerializer(many=True, read_only=True)
    class Meta:
        model= StreamPlatform
        fields= "__all__"