"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


# table Compte classe
class compte(Base):
    __tablename__ = 'compte'
    ID = Column(Integer, primary_key=True)
    Nom = Column(String)
    Owner = Column(String)
    User = Column(String)
    Password = Column(String)
    Namespace = Column(String)

    def __repr__(self):
        return "ID='{}', Nom='{}', Owner='{}', User='{}', Password='{}', Namespace='{}'\n"\
                .format(self.ID, self.Nom, self.Owner, self.User, self.Password, self.Namespace)
