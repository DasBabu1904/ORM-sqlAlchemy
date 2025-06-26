from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from create_tables import students

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)
conn = engine.connect()

def insertStudent():
    # insStuQ = students.insert().values(
    #     name="devi",
    #     lastname="kumari",
    #     age=24
    # )
    # result = conn.execute(insStuQ)
    # conn.commit()  # This saves the changes to database
    # print(result)
    conn.execute(students.insert(), [
        {'name':'Rajiv', 'lastname' : 'Khanna'},
        {'name':'Komal','lastname' : 'Bhandari'},
        {'name':'Abdul','lastname' : 'Sattar'},
        {'name':'Priya','lastname' : 'Rajhans'},
    ])
    conn.commit()