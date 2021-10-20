#!/usr/bin/env python3.9

from datetime import datetime
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.sql.sqltypes import BOOLEAN, BigInteger, Boolean, DateTime
import argparse
from sqlalchemy.orm import sessionmaker
import re
from tabulate import tabulate

Base = declarative_base()


class TestTask(Base):
    __tablename__ = "Testtasks"
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    status = Column(Boolean, nullable=False, server_default=expression.false())



def main():
    engine = create_engine(
        "mysql+mysqlconnector://root:Rahul12@localhost/mydatabase")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
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
        "--edit-title", nargs="?",const="Edit_title", help="Update Title name by taskid"
    )
    my_parser.add_argument(
        "--edit-status", nargs="?", const="Edit_status", help="Update title <complete><incomplete>"
    )
    my_parser.add_argument("-id", nargs=1,type=int, help = "Id of editing title or status")

    my_parser.add_argument("-title", nargs="*",type=str, help = "Updated title name")
    
    my_parser.add_argument("-iscomplete", nargs=1, type = str,choices=['True','False'], help= "updated status")
    my_parser.add_argument(
        "--delete", nargs="+", help="Delete task based on taskid provided"
    )
    my_parser.add_argument("--search", nargs="*",
                           help="Search title based on search")
    args = my_parser.parse_args()
    if args.list:
        if args.list and args.start and not args.end:
            startdate = args.start[0] + " 00:00:00"
            result = sess.query(TestTask).where(
                TestTask.created_at >= startdate)
        elif args.list and args.end and not args.start:
            enddate = args.end[0] + " 23:59:59"
            result = sess.query(TestTask).where(TestTask.created_at <= enddate)
        elif args.list and args.start and args.end:
            startdate = args.start[0] + " 00:00:00"
            enddate = args.end[0] + " 23:59:59"
            result = sess.query(TestTask).where(
                TestTask.created_at >= startdate,
                TestTask.created_at <= enddate
            )
        elif args.list == "All":
            result = sess.query(TestTask)
        elif args.list == "complete":
            result = sess.query(TestTask).where(TestTask.status == 1)
        elif args.list == "incomplete":
            result = sess.query(TestTask).where(TestTask.status == 0)
        print(
            tabulate(
                [
                    (   
                        item.id,
                        item.title,
                        item.created_at,
                    )
                    for item in result
                ],
                headers=["Id","Title", "Created_at"],
                tablefmt="psql",
            )
        )
    elif args.create:
        entry = TestTask(title=" ".join(args.create),
                         created_at=datetime.now())
        sess.add(entry)
        sess.commit()
    elif args.edit_title and args.id and args.title:
        result = sess.query(TestTask).get(args.id)
        result.title = " ".join(args.title)
        sess.commit()
    elif args.edit_status and args.id and args.iscomplete:
        result = sess.query(TestTask).get(args.id[0])
        if args.iscomplete[0] == "True": iscomplete = 1 
        else: iscomplete=0 
        result.status = iscomplete
        if iscomplete:
            result.completed_at = datetime.now()
        else:
            result.completed_at = None
        sess.commit()
    elif args.delete:
        for id in args.delete:
            result = sess.query(TestTask).get(id)
            sess.delete(result)
            sess.commit()
    elif args.search:
        result = sess.query(TestTask)
        title_list = [item.title for item in result]
        comp_patt = re.compile((args.search[0]).lower())
        title_in_search = []
        for title_name in title_list:
            z = comp_patt.findall(r'^.*'+title_name.lower(), re.IGNORECASE)
            if z:
                title_in_search += [[title_name]]
        print("Title with matching Pattern are ")
        print(tabulate(title_in_search, headers=["Title"], tablefmt="psql"))

if __name__ == "__main__":
    main()