import pandas as pd
import os
from glob import glob

# Gender, Age, Race, Pre-Processing
PATH = "/Users/janu/Documents/UCM/Spring_2023/NeuralNetworks/project/Frames"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

data=[]
for file in all_csv_files:
    df=pd.read_csv(file)
    data.append([file.rsplit('/', 2)[1],df['dominant_race'].mode().iloc[0],df['dominant_gender'].mode().iloc[0],round(df['age'].mean())])

gender_df = pd.DataFrame(data, columns=['video_ID', 'Race','Gender','Age'])
gender_df.to_csv("data/gender.csv", sep='\t', encoding='utf-8',index=False)


# YouTube Metadata Pre-Processing
youtube_df = pd.read_csv('data/raw_data.csv',delimiter='\t',encoding='utf-8')
del youtube_df['channelId']
del youtube_df['categoryId']
del youtube_df['title']
del youtube_df['description']
del youtube_df['contentDuration']
del youtube_df['contentDimension']
del youtube_df['contentDefinition']
del youtube_df['contentCaption']
del youtube_df['contentRating']
del youtube_df['favoriteCount']
del youtube_df['topicIds']
del youtube_df['relevantTopicIds']
del youtube_df['channelPublishedat']
del youtube_df['channelTitle']
del youtube_df['dislikeCount']
del youtube_df['subtitle']

for index, row in youtube_df.iterrows():
    if row['video_ID'] in gender_df.values:
        print(row['video_ID'])
        youtube_df.loc[index,'Gender']=gender_df.loc[gender_df['video_ID'] == row['video_ID'], 'Gender'].iloc[0]
        print(gender_df.loc[gender_df['video_ID'] == row['video_ID'], 'Gender'].iloc[0])
        youtube_df.loc[index,'Race']=gender_df.loc[gender_df['video_ID'] == row['video_ID'], 'Race'].iloc[0]
        youtube_df.loc[index,'Age']=gender_df.loc[gender_df['video_ID'] == row['video_ID'], 'Age'].iloc[0]
    else:
        youtube_df.loc[index,'Gender']="No Actor"
        youtube_df.loc[index,'Race']="No Actor"
        youtube_df.loc[index,'Age']=0


youtube_df["Age"] = youtube_df['Age'].astype('int')
youtube_df["viewCount"] = youtube_df['viewCount'].astype('int')
youtube_df["likeCount"] = youtube_df['likeCount'].astype('int')
youtube_df["commentCount"] = youtube_df['commentCount'].astype('int')
youtube_df["channelViewCount"] = youtube_df['channelViewCount'].astype('int')
youtube_df["channelSubscriberCount"] = youtube_df['channelSubscriberCount'].astype('int')

for index, row in youtube_df.iterrows():
    if  row["viewCount"]>=12000:
         youtube_df.loc[index,'views']='high'
    else:
         youtube_df.loc[index,'views']='low'

del youtube_df['video_ID']
youtube_df.to_csv("data/processed_data.csv", sep='\t', encoding='utf-8',index=False)