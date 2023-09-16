#!/usr/bin/python3
"""Lists all states with a name starting with 'N'.

Lists from the database hbtn_0e_0_usa where name matches the argument.
But this time, script is safe from MySQL injections!
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    state_name_searched = args[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cursor = connection.cursor()

    query = "SELECT *\
        FROM states\
        WHERE states.name LIKE BINARY %s\
        ORDER BY id ASC"

    cursor.execute(query, (state_name_searched + "%",))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
