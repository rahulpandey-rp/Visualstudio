import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestSqlalchemy(unittest.TestCase):
    def setup(self):
        self.engine = create_engine(
            "mysql+mysqlconnector://root:Rahul12@localhost/mydatabase")
        #Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.sess = self.Session()

class TestMain(unittest.TestCase):
    pass