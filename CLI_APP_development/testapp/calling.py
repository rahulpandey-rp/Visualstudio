import mysql.connector as sql_conn
import argparse
from tabulate import tabulate


class MysqlDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.table_name = 'task'

    def create_db(self):
        mycursor.execute(f"CREATE DATABASE {self.db_name}")

    def delete_db(self):
        mycursor.execute(f"DROP DATABASE {self.db_name}")

    def use_db(self):
        mycursor.execute(f"USE {self.db_name}")

    def add_table(self):
        mycursor.execute(
            f"create TABLE {self.table_name}  \
            (TaskId bigint(11) unsigned NOT NULL AUTO_INCREMENT, \
            Title VARCHAR(60) NOT NULL, \
            Created_at datetime NOT NULL, \
            Completed_at datetime NULL, \
            Status BOOLEAN NOT NULL default 0 , \
            Description text , \
            PRIMARY KEY (TaskId), UNIQUE (Title)) AUTO_INCREMENT = 1"
        )

    def add_data(self, title):
        zee = f"insert into {self.table_name} \
                values (default, '{title}', \
                now(), NULL, 0, 'NULL')"
        mycursor.execute(zee)
        mydb.commit()

    def update_status(self, taskid, update_status):
        mycursor.execute(
            f"Update {self.table_name} SET Status = {update_status}, \
                        Completed_at  = now() \
                        WHERE TaskId = {taskid}"
        )
        mydb.commit()

    def update_title(self, taskid, updated_title):
        mycursor.execute(
            f"Update {self.table_name} \
            SET Status = {updated_title} WHERE TaskId = {taskid}"
        )
        mydb.commit()

    def fetch_data(self):
        mycursor.execute(f"select * from {self.table_name}")
        result = mycursor.fetchall()
        return result

    def fetch_complete(self):
        mycursor.execute(f"select * from {self.table_name} WHERE Status = 1")
        result = mycursor.fetchall()
        return result

    def fetch_incomplete(self):
        mycursor.execute(f"select * from {self.table_name} WHERE Status = 0")
        result = mycursor.fetchall()
        return result

    def remove_data(self, taskids):
        for taskid in taskids:
            mycursor.execute(f"delete FROM {self.table_name} WHERE taskid = {taskid}")
        mydb.commit()


def listdatabase(fetch="All"):
    if fetch == "All":
        result = d1.fetch_data()
    elif fetch == "Complete":
        result = d1.fetch_complete()
    elif fetch == "Incomplete":
        result = d1.fetch_incomplete()
    else:
        print("Wrong Entry")
        return
    print(result)
    print(tabulate(result, tablefmt= 'psql' ))


if __name__ == "__main__":
    mydb = sql_conn.connect(host="localhost", user="root", passwd="Rahul12")
    mycursor = mydb.cursor()
    d1 = MysqlDatabase("mydatabase")
    d1.use_db()
    my_parser = argparse.ArgumentParser(
                                    allow_abbrev=False,
                                    description="This is a CLI app for to-do List"
                                    )
    my_parser.add_argument(
                        "--list", type=str, const="All",
                        nargs="?", choices=["All", "Incomplete", "Complete"],
                        help="List all the task respective to choices"
                        )
    my_parser.add_argument(
                            "--create", type=str,
                            nargs="+",
                            help="Create new title (Duplicate not allowed)"
                        )
    my_parser.add_argument(
                            "--edit-title",
                            nargs=2,
                            help="Update Title name by taskid"
                        )
    my_parser.add_argument(
                            "--edit-status",
                            nargs=2,
                            help="Update title <complete><incomplete>"
                        )
    my_parser.add_argument(
                            "--delete", nargs="+",
                            help="Delete task based on taskid provided"
                        )
    my_parser.add_argument("--search")
    args = my_parser.parse_args()
    if args.list:
        listdatabase(args.list)
    elif args.create:
        d1.add_data(
            title=" ".join(args.create)
        )
    elif args.edit_title:
        d1.update_title(args.edit_title[0], args.edit_title[1:])
    elif args.edit_status:
        d1.update_status(args.edit_status[0], args.edit_status[1])
    elif args.delete:
        d1.remove_data(args.delete)
