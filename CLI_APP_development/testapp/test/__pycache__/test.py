import mysql.connector as sql_conn
import argparse

class MysqlDatabase:
    def __init__(self,db_name):
        self.db_name = db_name

    def create_db(self):
        mycursor.execute(f"CREATE DATABASE {self.db_name}")
    
    def delete_db(self):
        mycursor.execute(f"DROP DATABASE {self.db_name}")

    def use_db(self):
        mycursor.execute(f"USE {self.db_name}")

    def add_table(self,table):
        mycursor.execute(f"create TABLE {table}  \
            (TaskId bigint(11) unsigned NOT NULL AUTO_INCREMENT, \
            Title VARCHAR(60) NOT NULL, \
            Created_at datetime NOT NULL, \
            Completed_at datetime NULL, \
            Status BOOLEAN NOT NULL default 0 , \
            Description text , \
            PRIMARY KEY (TaskId), UNIQUE (Title)) AUTO_INCREMENT = 1" )

    def add_data(self, *args, **kwargs):
        zee = (f"insert into {kwargs['table']} \
                values ({kwargs['id']}, \'{kwargs['title']}\', \
                now(),null, {kwargs['status']}, \'{kwargs['Description']}\')")
        mycursor.execute(zee)
        mydb.commit()

    def update_status(self, table, taskid, update_status):
        mycursor.execute(
                        f"Update {table} SET Status = {update_status}, \
                        Completed_at  = now() \
                        WHERE TaskId = {taskid}"
                        )
        mydb.commit()

    def update_title(self, table, taskid, updated_title):
        mycursor.execute(f"Update {table} SET Status = {updated_title} WHERE TaskId = {taskid}")
        mydb.commit()

    def fetch_data(self, table):
        mycursor.execute(f"select * from {table}")
        result = mycursor.fetchall()
        return(result)

    def fetch_complete(self, table):
        mycursor.execute(f"select * from {table} WHERE Status = 1")
        result = mycursor.fetchall()
        return(result)

    def fetch_incomplete(self, table):
        mycursor.execute(f"select * from {table} WHERE Status = 0")
        result = mycursor.fetchall()
        return(result)
'''
d1 = MysqlDatabase("mydatabase")
d1.use_db()
d1.add_table("task")
d1.add_data(
                table = 'task',
                id= 'default',
                title = 'Sleep at night',
                created_at = 'now()',
                completed_at = 'NULL',
                status = 0,
                Description = 'Do your work for 1st day'
                )

d1.update_status("task", 5, 1)
#d1.fetch_data("task")
'''


def listdatabase(fetch = "All"):
    if fetch == "All":
        result = d1.fetch_data("task")
    elif fetch == "Complete":
        result = d1.fetch_complete("task")
    elif fetch == "Incomplete":
        result = d1.fetch_incomplete("task")
    else:
        print("Wrong Entry")
        return
    print(result)

if __name__ == "__main__":
    mydb = sql_conn.connect(host = 'localhost', user = 'root', passwd = "Rahul@12")
    mycursor = mydb.cursor()
    d1 = MysqlDatabase("mydatabase")
    d1.use_db()
    my_parser = argparse.ArgumentParser(allow_abbrev = False)
    subparser = my_parser.add_subparsers(dest='command')
    login = subparser.add_parser('--edit')
    my_parser.add_argument('--list' , default= "All")
    args = my_parser.parse_args()
    if args.list:
        listdatabase(args.list)
    