import sqlite3
import csv

# git config --global user.name "Yaman Devkota"
# git config --global user.email "yamandevkota.77@gmail.com"

def create_connection():
    try:
        conn = sqlite3.connect("users.sqlite3")
        return conn
    except Exception as e:
        print(e)

Input_String = """
Enter the option:
    1.CREATE TABLE
    2.DUMP users from csv INTO users TABLE
    3.ADD new users INTO users TABLE
    4.QUERY all users from TABLE
    5.QUERY users by if from TABLE
    6.QUERY specified no. of records from TABLE
    7.DELETE all users
    8.DELETE users by id
    9.UPDATE users
    10.Press any key to EXIT
"""

# command line application
def create_table(conn):
    CREATE_USERS_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255),
            email CHAR(255) NOT NULL,
            web text
        );
    """
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY)
    print("User table was created successfully.")

def read_csv():
    users = []
    with open("sample_users.csv", "r") as f:
        data =  csv.reader(f)
        for user in data:
            users.append(tuple(user))

    return users[1:]

def insert_users(con, users):
    user_add_query = """
        INSERT INTO users
        (
            first_name,
            last_name,
            company_name,
            address,
            city,
            county,
            state,
            zip,
            phone1,
            phone2,
            email,
            web
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
    """

    cur = con.cursor()
    cur.executemany(user_add_query, users)
    con.commit()
    print(f"{len(users)} users were imported successfully.")

def select_users(con):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM users")
    for user in users:
        print(user)

def select_user_by_id(con, user_id):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM users where id = ?;", (user_id,))
    for user in users:
        print(user)

def delete_users(con):
    cur = con.cursor()
    cur.execute("DELETE FROM users;")
    con.commit()
    print("All users were deleted successfully")

def delete_user_by_id(con, user_id):
    cur = con.cursor()
    user = cur.execute("DELETE FROM users where id=?",(user_id,))
    con.commit()
    print(f"User with id [{user_id}] was successfully deleted.")

def main():
    conn = create_connection()
    user_input = input(Input_String)
    if user_input == "1":
        create_table(conn)
    elif user_input == "2":
        users =read_csv()
        insert_users(conn, users)
    elif user_input == "3":
        pass
    elif user_input == "4":
        select_users(conn)
    elif user_input == "5":
        user_id = input("Enter the user id:")
        select_user_by_id(conn, user_id)
    elif user_input == "6":
        pass
    elif user_input == "7":
        delete_users(conn)
    elif user_input == "8":
        user_id = input("Enter the user id:")
        delete_user_by_id(conn, user_id)
        
        


if __name__ =="__main__":
    main()

