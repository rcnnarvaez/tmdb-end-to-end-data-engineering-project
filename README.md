# TMDb End To End Data Engineering Project

### Introduction

In this project, we will build and ETL(Extract, Transform, Load) pipeline using the "The Movie Database" TMDb API on AWS. The pipeline will retrieve data from the TMDb API, transform it to a desired format, and load it into an AWS data store. 

### Will add diagram ![example of image](https://github.com/rcnnarvaez/tmdb-end-to-end-data-engineering-project/blob/main/image-rendered.webp)

### About Dataset/API
This API contains information about... [TMDb API](https://github.com/rcnnarvaez/tmdb-end-to-end-data-engineering-project/blob/main/TMDb_API%20ETL%20Pipeline.jpeg).

### Services Used
1. **S3 (Simple Storage Service):** Amazon S3...
   
2. **AWS Lambda:** AWS lambda...

3. **Cloud Watch:** Amazon CloudWatch...

4. **Glue Crawler:** AWS Glue Crawler...

5. **Data Catalog:** AWS Glue Data Catalog...

6. **Amazon Athena:** Amazon Athena...

### Install Packages
```
pip install pandas
pip install numpy
pip instal ....
```
### Project Excecution Flow
Extract Data from API -> Lambda Trigger (every 1 hour) -> Run Extract Code -> Store Raw Data -> Trigger Transform Function -> Transform Data and Load it -> Query Using Athena
