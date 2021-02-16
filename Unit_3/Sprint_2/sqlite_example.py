"""SQLite3 - Example of a connection"""

import sqlite3
import queries as q

# Make connection
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

# Make a cursor
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

if __name__ == "__main__":
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])
    print(len(results))