from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets

# Create your views here.

@api_view(['GET'])
def movie_list(request, format=None):
    movie_list= WatchList.objects.all()
    serialized= WatchListSerializer(movie_list, many=True, context={'request': request})
    return Response(serialized.data)

@api_view(['GET'])
def movie_detail(request, pk, format=None):
    movie= WatchList.objects.get(pk=pk)
    serialized= WatchListSerializer(movie, context={'request': request})
    return Response(serialized.data) 

# @api_view(['GET', 'POST'])
# def stream_list(request, format=None):
#     if request.method== 'GET':
#         stream_list= StreamPlatform.objects.all()
#         serialized= StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)
    
#     elif request.method == 'POST':
#         _data= request.data
#         serialized= StreamPlatformSerializer(data=_data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,  status= status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request, pk, format=None):
#     try:
#         stream= StreamPlatform.objects.get(pk=pk)
        
#     except StreamPlatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#         serialized= StreamPlatformSerializer(stream)
#         return Response(serialized.data) 
    
#     elif request.method == 'PUT':
#         _data= request.data
#         serialized= StreamPlatformSerializer(stream, data= _data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         StreamPlatform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
     

# USING CLASS BASED API VIEW
# class StreamPlatformList(APIView):
#     def get(self, request, format=None):
#         stream_list= StreamPlatform.objects.all()
#         serialized= StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)
    
#     def post(self, request, format=None):
#         _data= request.data
#         serialized= StreamPlatformSerializer(data=_data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,  status= status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# class StreamPlatformDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         stream_platform= self.get_object(pk)
#         serialized= StreamPlatformSerializer(stream_platform)
#         return Response(serialized.data)
    
#     def put(self, request, pk, format=None):
#         stream_platform= self.get_object(pk)
#         _data= request.data
#         serialized= StreamPlatformSerializer(stream_platform, data= _data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         stream_platform= self.get_object(pk)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# MIXINS CLASS BASED VIEW
# class StreamPlatformList(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
#     queryset= StreamPlatform.objects.all()
#     serializer_class= StreamPlatformSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,                               
#                            generics.GenericAPIView):
#     queryset= StreamPlatform.objects.all()
#     serializer_class= StreamPlatformSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# GENRERIC CLASS BASED VIEW
# class StreamPlatformList(generics.ListCreateAPIView):
#     queryset= StreamPlatform.objects.all()
#     serializer_class= StreamPlatformSerializer
    
# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset= StreamPlatform.objects.all()
#     serializer_class=StreamPlatformSerializer
    
    
class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset= StreamPlatform.objects.all()
    serializer_class= StreamPlatformSerializer

    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('watchlist-list', request=request, format=format),
        'streamplatform': reverse('streamplatform-list', request=request, format=format)
    })