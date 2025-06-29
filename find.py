
from db_connection import conn
from insert import students

def findAllStudents():
    allStuQ=students.select()
    restult=conn.execute(allStuQ )
    stu_rows=restult.fetchall()
    print(stu_rows)

def findByname(name:str):
    nameQ=students.select().where(students.c.name==name)
    result=conn.execute(nameQ)
    row=result.fetchone()
    print(row)

