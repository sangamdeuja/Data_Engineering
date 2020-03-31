## Project: Data Modeling with Cassandra
### Problem Defination
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions.

### Project Overview
The main objective is to apply the knowledge of data modeling witha Apache Cassandra and complete ETL pipeline using Python. 

### Datasets
WE have event_data folder which contains the events in multiple csv file.

### Step 1 : Modeling NoSQL database
- CREATE KESPACE and SET KEYSPACE statements
- Develop CREATE statement for each of the tables to address each question
- Load the data with INSERT statement for each of the tables
- Use statements like IF NOT EXISTS, CREATE, DROP TABLE appropriately
- Test by running the proper select statements with the correct WHERE clause

### Step 2 : Build ETL Pipeline
- Iterate through each event file in event_data to process and create a new CSV file
- Load preprocessed records into relevant tables 
- Test by running SELECT statements after running the queries on the database
