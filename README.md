# TMDb End To End Data Engineering Project

### Introduction

In this project, we will build and ETL(Extract, Transform, Load) pipeline using the "The Movie Database" TMDb API on AWS. The pipeline will retrieve data from the TMDb API, transform it to a desired format, and load it into an AWS data store. 

### Architecture ![example of image](https://github.com/rcnnarvaez/tmdb-end-to-end-data-engineering-project/blob/main/TMDb_API%20ETL%20Pipeline.jpeg)

### Project Excecution Flow
Extract Data from API -> Lambda Trigger (every 1 hour) -> Run Extract Code -> Store Raw Data -> Trigger Transform Function -> Transform Data and Load it -> Query Using Athena

### About Dataset/API
This section contains the relevant information about the "The Movie Database" API and how to interact with it: [TMDb API](https://developer.themoviedb.org/docs/getting-started).

### Solution

I built a daily ETL pipeline to ingest movie data from the TMDb API. The goal was to extract the top-rated movies, polling parameters and transform the data into CSV format, and make it queryable using Athena.
I scheduled the pipeline using AWS EventBridge, which triggers the job daily.
The core processing happens in an AWS Lambda function that:
- Calls the TMDb API
- Loops through all 500 accessible pages
- Converts the JSON responses into CSV format
- Writes the output to an S3 bucket
  
Then, I used AWS Glue Crawlers to infer the schema and register the data in the Glue Data Catalog.
Finally, I queried the data using AWS Athena, which allows analysts to run SQL queries directly over the data in S3.

### Cleaned Data Sample ![TMDb cleaned data](https://github.com/rcnnarvaez/tmdb-end-to-end-data-engineering-project/blob/main/TMDb_cleaned_data.png)

### Services Used
1. **Amazon S3 (Simple Storage Service):** 
   
2. **AWS Lambda:** 

3. **Amazon Cloud Watch:** 

4. **AWS Glue Crawler:**

5. **AWS Glue Data Catalog:** 

6. **Amazon Athena:** 

### Install Packages and Imports
```
pip install pandas
pip install numpy
pip instal

import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd
import os
import requests
```
