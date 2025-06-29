from db_connection import conn
from insert import students

def DeleteByID(id:int):
    DelQ=students.delete().where(students.c.id==id)
    conn.execute(DelQ)
    conn.commit()
    