from sqlalchemy import create_engine, inspect
from sqlalchemy import text
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptConte

import os
import csv
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL= os.getenv("postgresql://exam_db_g0tz_user:i9s57LP0aSgXEz2PgM4KagtmPTNYN1Nk@dpg-cvsrkgq4d50c73d7c6p0-a.singapore-postgres.render.com/exam_db_g0tz") 
engine = create_engine(DATABASE_URL,  client_encoding='utf8')

connection = engine.connect()
asd = inspect(engine) 


print (asd.get_table_names())


result = connection.execute(
    text("""CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL;
    CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task VARCHAR(255) NOT NULL,
            deadline DATE(255),
            user VARCHAR(255) REFERENCES users(username)
);"""))


print( result )

x = connection.execute(
     text("""INSERT INTO users (username, password) VALUES ('reqw','reqw');
 ;"""))


q = connection.execute(
    text(""" SELECT * FROM users
    ;"""))

print(q.mappings().all())
print(q.fetchall())



connection.commit()