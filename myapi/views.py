from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from .models import dashcamvideo
from .serializers import dashcamvideoSerializer
import json

# Create your views here.
@api_view(["POST",])
def campost(request):
    num = dashcamvideo()
    if request.method  == "POST": 
        serializers = dashcamvideoSerializer(num,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse("done",safe=False)
        return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

@api_view(["POST",])
def camdetail(request):
    num = request.POST.get('imei')
    try:
        new = dashcam(imei=num)
        if request.method  == "POST": 
            serializers = dashcamSerializer(new,data=request.data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse("done",safe=False)
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["POST",])
def newuser(request):
    num = request.POST.get('imei')
    temp = dashcam()
    temp.imei = num
    temp.save()

@api_view(["POST",])
def event(request):
    imei = request.POST.get('imei')
    typei = request.POST.get('type')
    altype = request.POST.get('alarm_type')
    altime = request.POST.get('alarm_time')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    filelist = request.POST.get('file_list')
    dic = {}
    dic['type']='COMMAND'
    dic['imei']=imei
    dic['command']='some_command'
    return JsonResponse(json.dumps(dic))