from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL, echo=True)

# create Table

###-------------------Option:1-  Here table is created by meta, Table, and create all -----------------############
meta = MetaData()

students = Table(
    'students', meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("lastname", String),
    Column("age", Integer),
    Column("grade", String),
    Column("gender", String)
)

addresses = Table(
    'addresses', meta, 
    Column('id', Integer, primary_key = True), 
    Column('st_id', Integer), 
    Column('postal_add', String), 
    Column('email_add', String)
)
    

if __name__ == "__main__":
    meta.create_all(engine)
    print("Tables created successfully!")

############### -------- we can also do it by Base, class models  and create_alll --------------##########