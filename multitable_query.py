from db_connection import conn
from sqlalchemy import select
from insert import students, addresses

def multitable_query():
    s = select(students, addresses).where(students.c.id == addresses.c.st_id)
    result = conn.execute(s)
    for row in result:
        print(row)