from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os

DEVELOPER_KEY = os.environ['YOUTUBE_API']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def main():
    movie_title= input('Please enter movie title: ').upper()
    print(movie_trailer(movie_title))

def movie_trailer(movie):

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list(
            q= movie + ' Official Trailer', #adds "official trailer" on the movie title
            part='id, snippet',
            order='relevance',  #sort by relevance
            maxResults=1,   #get one result
            type='videos',
            #safeSearch='none'   #no restrictions on the videos
        ).execute()

        first_result = search_response.get('items', [])[0]
        
        title = first_result['snippet']['title']
        video_id = first_result['id']['videoId']

        return { 'title': title, 'video_id': video_id }
        

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
    