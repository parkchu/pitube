from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from youtube.models import Channel, Video
from .serializer import ChannelSerializer, VideoSerializer
from rest_framework.parsers import JSONParser
from account.models import User
@csrf_exempt
def channel_list(request):
    if request.method == 'GET':
        query_set = Channel.objects.all()
        serializer = ChannelSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChannelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def video_list(request):
    if request.method == 'GET':
        query_set = Video.objects.all()
        serializer = VideoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def channel(request, pk):

    obj = Channel.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ChannelSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        if data['whether'] == 'cancel':
            user = User.object.get(pk=data['user_id'])
            thisChannel = Channel.objects.get(pk=data['channel_id'])
            thisChannel.subscribe.remove(user)
        elif data['whether'] == 'subscribe':
            user = User.object.get(pk=data['user_id'])
            thisChannel = Channel.objects.get(pk=data['channel_id'])
            thisChannel.subscribe.add(user)
        return JsonResponse(data, safe=False)
@csrf_exempt
def video(request, pk):

    obj = Video.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = VideoSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        if data['whether'] == 'like':
            user = User.object.get(pk=data['user_id'])
            thisVideo = Video.objects.get(pk=data['video_id'])
            thisVideo.good.add(user)
        elif data['whether'] == 'dislike':
            user = User.object.get(pk=data['user_id'])
            thisVideo = Video.objects.get(pk=data['video_id'])
            thisVideo.good.remove(user)
        return JsonResponse(data, safe=False)
