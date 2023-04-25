from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import numpy as np
from youtube_transcript_api import YouTubeTranscriptApi

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps tab of https://cloud.google.com/console

DEVELOPER_KEY = "AIzaSyC3DbrwjWecRkb7IrnhvcMcIzXprga9kBw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_get_videoinfo(videoID):
    video = {}
    try:
        youtube =build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)     
    except:
        pass
    search_response={}
    try:
              video['subtitle'] = YouTubeTranscriptApi.get_transcript(videoID)
    except Exception as e:
             video['subtitle'] = ''
    
    search_response=youtube.videos().list(
      part="id, snippet,contentDetails,liveStreamingDetails,player,statistics,status, topicDetails",
      id=videoID
      ).execute()
    for item in search_response.get("items", []):   
      video['id']=item['id']
      video['channelId']=item['snippet']['channelId']
      video['channelTitle']=item['snippet']['channelTitle']
      video['categoryId']=item['snippet']['categoryId']
      video['title']=item['snippet']['title']
      video['description']=item['snippet']['description']
      
      channel_details=youtube.channels().list(id=video['channelId'],part="snippet,statistics").execute()
      for channel in channel_details.get("items",[]):
        try:
          video['channelPublishedat']=channel['snippet'].get('publishedAt', '')
          video['channelViewCount']=channel['statistics'].get('viewCount',0)
          video['channelSubscriberCount']=channel['statistics'].get('subscriberCount',0)
        except KeyError as e:
            print("An KeyError error %d occurred:\n%s",(e.resp.status, e.content))

      video['contentDuration']=item['contentDetails']['duration']
      video['contentDimension']=item['contentDetails']['dimension']
      video['contentDefinition']=item['contentDetails']['definition']
      video['contentCaption']=item['contentDetails']['caption']
      video['contentRating']=item['contentDetails'].get('contentRating',{})
      video['viewCount']=item['statistics'].get('viewCount',0)
      video['likeCount']=item['statistics'].get('likeCount',0)
      video['commentCount']=item['statistics'].get('commentCount',0)
      video['dislikeCount']=item['statistics'].get('dislikeCount',0)
      video['favoriteCount']=item['statistics'].get('favoriteCount',0)
      video['topicIds']=item.get('topicDetails',{}).get('topicIds','')
      video['relevantTopicIds']=item.get('topicDetails',{}).get('relevantTopicIds','')

    return video
  

df = pd.DataFrame()
df['video_ID']= pd.read_csv("Youtube_VideoIds.txt", header=None)
videoids = df['video_ID'].to_list()

df['channelId']=''
df['categoryId']=''
df['title']=''
df['description']=''
df['channelSubscriberCount']=''
df['contentDuration']=''
df['contentDimension']=''
df['contentDefinition']=''
df['contentCaption']=''
df['contentRating']=''
df['favoriteCount']=''
df['topicIds']=''
df['relevantTopicIds']=''

df['viewCount']=''
df['likeCount']=''
df['dislikeCount']=''
df['commentCount']=''
df['channelPublishedat']=''
df['channelTitle']=''
df['channelViewCount']=''

i=1
for videoid in videoids:
        videoinfo = youtube_get_videoinfo(videoid)
        print(i,videoid)
        df.loc[df['video_ID'] == videoid, 'viewCount'] = videoinfo.get('viewCount')
        df.loc[df['video_ID'] == videoid, 'likeCount'] = videoinfo.get('likeCount')
        df.loc[df['video_ID'] == videoid, 'dislikeCount'] = videoinfo.get('dislikeCount')
        df.loc[df['video_ID'] == videoid, 'commentCount'] = videoinfo.get('commentCount')
        df.loc[df['video_ID'] == videoid, 'channelPublishedat'] = videoinfo.get('channelPublishedat')
        df.loc[df['video_ID'] == videoid, 'channelTitle'] = videoinfo.get('channelTitle')
        df.loc[df['video_ID'] == videoid, 'channelViewCount'] = videoinfo.get('channelViewCount')
        df.loc[df['video_ID'] == videoid, 'channelId'] = videoinfo.get('channelId')
        df.loc[df['video_ID'] == videoid, 'categoryId'] = videoinfo.get('categoryId')
        df.loc[df['video_ID'] == videoid, 'title'] = videoinfo.get('title')
        df.loc[df['video_ID'] == videoid, 'description'] = videoinfo.get('description')
        df.loc[df['video_ID'] == videoid, 'channelSubscriberCount'] = videoinfo.get('channelSubscriberCount')
        df.loc[df['video_ID'] == videoid, 'contentDuration'] = videoinfo.get('contentDuration')
        df.loc[df['video_ID'] == videoid, 'contentDimension'] = videoinfo.get('contentDimension')
        df.loc[df['video_ID'] == videoid, 'contentDefinition'] = videoinfo.get('contentDefinition')
        df.loc[df['video_ID'] == videoid, 'contentCaption'] = videoinfo.get('contentCaption')
        df.loc[df['video_ID'] == videoid, 'contentRating'] = videoinfo.get('contentRating')
        df.loc[df['video_ID'] == videoid, 'favoriteCount'] = videoinfo.get('favoriteCount')
        df.loc[df['video_ID'] == videoid, 'topicIds'] = videoinfo.get('topicIds')
        df.loc[df['video_ID'] == videoid, 'relevantTopicIds'] = videoinfo.get('relevantTopicIds')
       
        raw_subtitles_lst=videoinfo.get('subtitle')
        subtitles_lst=[]
        if raw_subtitles_lst is not None:  
          for indx in raw_subtitles_lst:
            subtitles_lst.append(indx['text'].replace('\n', ''))
      
        df.loc[df['video_ID'] == videoid, 'subtitle'] = ' '.join(subtitles_lst)
        i=i+1

df.dropna(subset=['subtitle'],inplace=True)    
df.to_csv("data/youtube_metadata.csv", sep='\t', encoding='utf-8',index=False)
   