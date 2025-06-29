from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from create_tables import students, addresses

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

def insertAddress():
    conn.execute(addresses.insert(), [
       {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
       {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
       {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
       {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
       {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
    ])
    conn.commit()