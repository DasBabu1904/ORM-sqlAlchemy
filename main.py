from sqlalchemy import create_engine
from sqlalchemy import MetaData
from dotenv import load_dotenv
import os
from sqlalchemy import Table, Column, Integer, String, MetaData
from insert import insertStudent,insertAddress
import find
import update
import delete
from multitable_query import multitable_query
load_dotenv()  # take environment variables from .env file
DB_URL=os.getenv("DATABASE_URL")
# print(DB_URL)
engine = create_engine(DB_URL,echo = True)

# insertStudent()
# Application logic goes here
# Tables are created separately using create_tables.py

# find.findAllStudents()
# find.findByname("devi")
# update.updateStudentName("Priya","DaDa")
# delete.DeleteByID(10)
# insertAddress()
multitable_query()