from django.shortcuts import render
import requests
from .models import APIData
from googleapiclient.discovery import build
import pandas as pd
import threading
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import DataSerializer

# @csrf_exempt
# def departmentApi(request,id=0):
#     if request.method=='GET':
#         departments = APIData.objects.all()
#         departments_serializer=DataSerializer(departments,many=True)
#         return JsonResponse(departments_serializer.data,safe=False)






# putting api and making youtub build

api_key = 'AIzaSyD614qA-m4LXimwdSo9kqoW1BaPOOMZujg'

youtube = build('youtube', 'v3', developerKey=api_key)


# query to fetch the desired field and store it in database 

def savedata():

    all_data = []
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        order="date",
        q="cat",
        maxResults=1,
        fields="items(id(videoId),snippet(publishedAt,title,description,thumbnails))"
        
)
    response = request.execute()

    for i in range(len(response['items'])):
        vid_id = response['items'][i]['id']['videoId']
        vid_title = response['items'][i]['snippet']['title'],
        vid_publishDate = response['items'][i]['snippet']['publishedAt'],
        vid_description = response['items'][i]['snippet']['description'],
        logo_url = response['items'][i]['snippet']['thumbnails']['default']['url'],
        data= APIData(vid_id = vid_id ,vid_title = vid_title , vid_publishDate=vid_publishDate ,vid_description = vid_description ,logo_url=logo_url)
        data.save()

    # to run every 20 sec
    threading.Timer(5, savedata).start()


# homepage called at start
@csrf_exempt
def getData(request):
    if request.method=='GET':
        departments = APIData.objects.all()
        departments_serializer=DataSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)


def index(request):
    savedata()

    return render(request , 'index.html') 