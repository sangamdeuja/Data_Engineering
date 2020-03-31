# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    start_time bigint,
    user_id int,
    level VARCHAR(10),
    song_id VARCHAR(20),
    artist_id VARCHAR(20),
    session_id INTEGER,
    location VARCHAR(50),
    user_agent VARCHAR(150)
);
""")


user_table_create = ("CREATE TABLE users (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);")


song_table_create = ("CREATE TABLE songs (song_id varchar, title varchar, artist_id varchar, year int, duration int);")


artist_table_create = ("CREATE TABLE artists (artist_id varchar, name varchar, location varchar,latitude varchar, longitude varchar);")


time_table_create = ("CREATE TABLE time (start_time bigint, hour int, day varchar,week int, month varchar, year int, weekday varchar);")


# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id) DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name , gender, level) VALUES (%s, %s, %s, %s, %s);""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert =("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);""")



time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""SELECT song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]