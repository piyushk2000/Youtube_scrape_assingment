from googleapiclient.discovery import build
import pandas as pd
import json

api_key = 'AIzaSyD614qA-m4LXimwdSo9kqoW1BaPOOMZujg'


youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_stats(youtube):
    all_data = []
request = youtube.search().list(
        part="id,snippet",
        type='video',
        order="date",
        q="cat",
        maxResults=2,
        fields="items(id(videoId),snippet(publishedAt,title,description,thumbnails))"
)

response = request.execute()

data= request.execute() 
# r = json.dumps(data)

# response = -json.loads(r)
# response = data.json()


    
    # for i in range(len(response['items'])):
    #     data = dict(vid_id = response['items'][i]['id']['videoId'],
    #                 vid_title = response['items'][i]['snippet']['title'],
    #                 vid_publishDate = response['items'][i]['snippet']['publishedAt'],
    #                 vid_description = response['items'][i]['snippet']['description'],
    #                 logo_url = response['items'][i]['snippet']['thumbnails']['default']['url'],
    #                 )
    #     all_data.append(data)

    # return all_data

vid_id_list = []
vid_title_list = []
vid_publishDate_list = []
vid_description_list = []
logo_url_list = []


for i in range(len(response['items'])):
    vid_id = response['items'][i]['id']['videoId']
    vid_title = response['items'][i]['snippet']['title'],
    vid_publishDate = response['items'][i]['snippet']['publishedAt'],
    vid_description = response['items'][i]['snippet']['description'],
    logo_url = response['items'][i]['snippet']['thumbnails']['default']['url'],
    # vid_id_list.append(vid_id)
    # vid_title_list.append(vid_title)
# for i in range(len(response['items'])):
#     x = response['items'][i]['id']['videoId'],
#     y = response['items'][i]['snippet']['title'],
#     name_list.append(x)
#     home_list.append(y)


# video_statistics = get_video_stats(youtube)
# video_data = pd.DataFrame(video_statistics)

# video_data['vid_publishDate'] = pd.to_datetime(video_data['vid_publishDate'])

# video_data = video_data.sort_values(by=['vid_publishDate'] , ascending=False)