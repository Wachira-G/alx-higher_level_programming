#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

if __name__ == "__main__":

    import MySQLdb
    import sys

    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    state_name = args[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cursor = connection.cursor()

    query = "SELECT cities.name\
        FROM cities\
        JOIN states ON states.id = cities.state_id\
        WHERE states.name like %s\
        ORDER BY cities.id ASC"
    cursor.execute(query, (state_name + "%",))

    query_rows = cursor.fetchall()
    strin = ", ".join([i[0] for i in list(query_rows)])
    print(strin)

    cursor.close()
    connection.close()
