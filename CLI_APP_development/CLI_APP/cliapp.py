from datetime import datetime
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.sql.sqltypes import BigInteger, Boolean, DateTime
import argparse
from sqlalchemy.orm import sessionmaker
import re
from tabulate import tabulate
import sqlalchemy.orm.exc

Base = declarative_base()


class TestTask(Base):
    __tablename__ = "Testtasks"
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    title = Column(String(30), unique=True, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    status = Column(Boolean, nullable=False, server_default=expression.false())


class TodoManager:
    format = "%Y-%m-%d %H:%M:%S"
    dateformat = "%Y-%m-%d"
    def __init__(self):
        engine = create_engine(
            "mysql+mysqlconnector://root:Rahul12@localhost/mydatabase"
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.sess = Session()

    def list_all(self):
        result = self.sess.query(TestTask)
        TodoManager.print_table(result)

    def list_complete(self):
        result = self.sess.query(TestTask).where(TestTask.status == 1)
        print("Task with Status incomplete")
        TodoManager.print_table(result)

    def list_incomplete(self):
        result = self.sess.query(TestTask).where(TestTask.status == 0)
        print("Task with Status incomplete")
        TodoManager.print_table(result)

    def list_start_end(self, start, end):
        startdate = start + " 00:00:00"
        enddate = end + " 23:59:59"
        try:
            res = bool(datetime.strptime(startdate, TodoManager.format))
            res = bool(datetime.strptime(enddate, TodoManager.format))
        except ValueError as ve:
            print(ve)
            print(f"Please enter date in right format {TodoManager.dateformat}")
        else:
            result = self.sess.query(TestTask).where(
                TestTask.created_at >= startdate, TestTask.created_at <= enddate
                )
            TodoManager.print_table(result)

    def list_start(self, start):
        startdate = start + " 00:00:00"
        try:
            res = bool(datetime.strptime(startdate, TodoManager.format))
        except ValueError as ve:
            print(ve)
            print(f"Please enter date in right format")
        else:
            result = self.sess.query(TestTask).where(
                TestTask.created_at >= startdate)
            TodoManager.print_table(result)

    def list_end(self, end):
        enddate = end + " 23:59:59"
        try:
            res = bool(datetime.strptime(enddate, TodoManager.format))
        except ValueError as ve:
            print(ve)
            print(f"Please enter date in right format {TodoManager.dateformat}")
        else:
            result = self.sess.query(TestTask).where(
                TestTask.created_at <= enddate)
            TodoManager.print_table(result)

    def create_title(self, add_title):
        entry = TestTask(title=add_title, created_at=datetime.now())
        self.sess.add(entry)
        self.sess.commit()
        print("New title added")

    def edit_title(self, id, updated_title):
        result = self.sess.query(TestTask).get(id)
        try:
            result.title = updated_title
        except AttributeError as ae:
            print("Id not found: id doesnot exist in table")
        else:
            result.updated_at = datetime.now()
            self.sess.commit()
            print("Title updated")

    def edit_status(self, id, iscomplete):
        result = self.sess.query(TestTask).get(id)
        if iscomplete == "True":
            iscomplete = 1
        elif iscomplete == "False":
            iscomplete = 0
        try :
            result.status = iscomplete
        except AttributeError as ae:
            print("Id not found: id doesnot exist in table")
        else:
            if iscomplete:
                result.completed_at = datetime.now()
                result.updated_at = datetime.now()
            else:
                result.completed_at = None
                result.updated_at = datetime.now()
            self.sess.commit()
            print("status Updated")

    def delete_entry(self, tasks):
        confirm = input("Do you really want to delete [y/n]: ")
        if confirm == "Y" or confirm == "y":  
            for id in tasks:
                result = self.sess.query(TestTask).get(id)
                try:
                    self.sess.delete(result)
                except sqlalchemy.orm.exc.UnmappedInstanceError as maperror:
                    print(maperror)
                    print("Entry not found to delete.")
                else:
                    self.sess.commit()
                    print("Task deleted")
        elif confirm == "N" or confirm == "n":
            print("Task not deleted")
        

    def search_titlebyword(self, search_word):
        result = self.sess.query(TestTask)
        title_list = [item.title for item in result]
        comp_patt = re.compile((search_word).lower())
        title_in_search = []
        for title_name in title_list:
            z = comp_patt.findall(r"^.*" + title_name.lower(), re.IGNORECASE)
            if z:
                title_in_search += [[title_name]]
        print("Title with matching Pattern are ")
        print(tabulate(title_in_search, headers=["Title"], tablefmt="psql"))
    
    @classmethod
    def print_table(cls, result):
        print(
            tabulate(
                [
                    (
                        item.id,
                        item.title,
                        item.created_at,
                        item.status,
                    )
                    for item in result
                ],
                headers=["Id", "Title", "Created_at", "Iscomplete"],
                tablefmt="psql",
            )
        )


def main():

    my_parser = argparse.ArgumentParser(
        allow_abbrev=False, description="This is a CLI app for to-do List"
    )
    my_parser.add_argument(
        "--list",
        type=str,
        const="All",
        nargs="?",
        choices=[
            "All",
            "incomplete",
            "complete",
        ],
        help="List all the task respective to choices",
    )
    my_parser.add_argument("--start", nargs=1, type=str)
    my_parser.add_argument("--end", nargs=1, type=str)
    my_parser.add_argument(
        "--create", type=str, nargs="+",
        help="Create new title (Duplicate not allowed)"
    )
    my_parser.add_argument(
        "--edit-title",
        nargs="?",
        const="Edit_title",
        help="Update Title name by taskid",
    )
    my_parser.add_argument(
        "--edit-status",
        nargs="?",
        const="Edit_status",
        help="Update title <complete><incomplete>",
    )
    my_parser.add_argument(
        "-id", nargs=1, type=int, help="Id of editing title or status"
    )

    my_parser.add_argument("-title", nargs="*", type=str,
                           help="Updated title name")

    my_parser.add_argument(
        "-iscomplete",
        nargs=1,
        type=str,
        choices=["True", "False"],
        help="updated status",
    )
    my_parser.add_argument(
        "--delete", nargs="+", help="Delete task based on taskid provided"
    )
    my_parser.add_argument("--search", nargs="*",
                           help="Search title based on search")
    args = my_parser.parse_args()

    if args.list:
        list = TodoManager()
        if args.list and args.start and not args.end:
            list.list_start(args.start[0])
        elif args.list and args.end and not args.start:
            list.list_end(args.end[0])
        elif args.list and args.start and args.end:
            list.list_start_end(args.start[0], args.end[0])
        elif args.list == "All":
            list.list_all()
        elif args.list == "complete":
            list.list_complete()
        elif args.list == "incomplete":
            list.list_incomplete()

    elif args.create:
        create = TodoManager()
        create.create_title(" ".join(args.create))

    elif args.edit_title and args.id and args.title:
        update_title = TodoManager()
        update_title.edit_title(args.id, " ".join(args.title))

    elif args.edit_status and args.id and args.iscomplete:
        update_status = TodoManager()
        update_status.edit_status(args.id[0], args.iscomplete[0])
        

    elif args.delete:
        delete_task = TodoManager()
        delete_task.delete_entry(args.delete)
        

    elif args.search:
        search_title = TodoManager()
        search_title.search_titlebyword(" ".join(args.search))


if __name__ == "__main__":
    main()
