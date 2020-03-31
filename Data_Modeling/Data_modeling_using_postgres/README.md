# Project : Data Modeling with Postgres

### Problem Defination:
**Sparkify**, a start-up company, has collected the data from their application. Those data are songs and logs files in json format. They want to generate the relational database schema and ETL pipeline for the analytics purpose. Data Engineer is reponsible to test database and ETL pipeline by running queries given to you by the analytics team from Sparkify.

### Database Schema design building ETL pipeline

We adopted star schema in which we generated one fact table and four dimension tables:
- **Fact Table** : songplays
- **Dimension Table**: users,songs,artists and time

The features(columns) of tables in the database is intialized, the structure of which is available in **crate_tables.py**. All the processes involved for reading the files and loading them in the tables are clearly shown in **etl.ipynb** notebook. All the queries required to generate those tables are available in **sql_queries.py**.The same processes are well structured to process entire dataset making it a pipeline,the **etl.py** file. In order to monitor the entire processed a **test.ipynb** has been created which can be tested in several intermediate steps. 

### Python Script to generate the schema: 

python create_tables.py
python et.py

