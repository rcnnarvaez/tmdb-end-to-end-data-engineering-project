import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd

def top_movies(all_results):
    top_movies_list = []
    for row in all_results[:]:
        original_title = row['original_title']
        title = row['title']
        original_language = row['original_language']
        id_number = row['id']
        movie_element = {'original_title':original_title, 'title':title, 'original_language':original_language, 
                        'id':id_number}
        top_movies_list.append(movie_element)
    return top_movies_list

def movie_data(all_results):
    movie_data_list = []
    for row in all_results[:]:
        title = row['title']
        vote_count= row['vote_count']
        vote_average = row['vote_average']
        popularity = row['popularity']
        release_date = row['release_date']
        movie_data_element = {'title': title, 'vote_count': vote_count, 'vote_average': vote_average,
                            'popularity': popularity, 'release_date': release_date}
        movie_data_list.append(movie_data_element)
    return movie_data_list

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucket = "tmdb-etl-project-narvaez"
    Key = "raw_data/to_processed/"

    tmdb_results = []
    tmdb_keys = []
    for file in s3.list_objects(Bucket = Bucket, Prefix = Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1] == "json":
            response = s3.get_object(Bucket = Bucket, Key = file_key)
            content = response['Body']
            jsonObject = json.loads(content.read())
            tmdb_results.append(jsonObject)
            tmdb_keys.append(file_key)

    for all_results in tmdb_results:
        top_movies_list = top_movies(all_results)
        movie_data_list = movie_data(all_results)

        top_movies_df = pd.DataFrame.from_dict(top_movies_list)
        top_movies_df = top_movies_df.drop_duplicates(subset=['id'])

        movie_data_df = pd.DataFrame.from_dict(movie_data_list)
        movie_data_df = movie_data_df.drop_duplicates(subset=['title'])
        movie_data_df['release_date'] = pd.to_datetime(movie_data_df['release_date'])

        top_movies_key = "transformed_data/top_movies_list/top_movies_transformed_" + str(datetime.now()) + ".csv"
        top_movies_buffer = StringIO()
        top_movies_df.to_csv(top_movies_buffer, index = False)
        top_movies_content = top_movies_buffer.getvalue()
        s3.put_object(Bucket = Bucket, Key = top_movies_key, Body = top_movies_content)

        movie_data_key = "transformed_data/movie_data_list/movie_data_transformed_" + str(datetime.now()) + ".csv"
        movie_data_buffer = StringIO()
        movie_data_df.to_csv(movie_data_buffer, index = False)
        movie_data_content = movie_data_buffer.getvalue()
        s3.put_object(Bucket = Bucket, Key = movie_data_key, Body = movie_data_content)

    s3_resource = boto3.resource('s3')
    for key in tmdb_keys:    
        copy_source = {
            'Bucket': Bucket,
            'Key': key
        }        
        s3_resource.meta.client.copy(copy_source, Bucket, 'raw_data/processed/' + key.split("/")[-1])
        s3_resource.Object(Bucket, key).delete()
        

        
     
