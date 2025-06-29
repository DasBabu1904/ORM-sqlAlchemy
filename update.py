from db_connection import conn
from insert import students

def updateStudentName(name:str,newname):
    nameQ=students.update().where(students.c.name==name).values(name=newname)
    conn.execute(nameQ)
    conn.commit()
    s = students.select()
    conn.execute(s).fetchall()