import json
import os
import requests
import time
import boto3
from datetime import datetime

def lambda_handler(event, context):
    Authorization = os.environ["Authorization"]

    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {Authorization}"
    }
    all_results = []

    page = 1
    response = requests.get(f"{url}&page={page}", headers=headers)
    data = response.json()

    total_pages = data["total_pages"]
    all_results.extend(data["results"])

    max_pages = min(total_pages,5)

    for page in range(2, max_pages + 1):
        response = requests.get(f"{url}&page={page}", headers=headers)
        data = response.json()
        all_results.extend(data["results"])
        time.sleep(.25)
 
    client = boto3.client('s3')
    filename = "all_results_" + str(datetime.now())+ ".json"

    client.put_object(
        Bucket = "tmdb-etl-project-narvaez",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(all_results)
    ) 