from sqlalchemy import Column, Integer, String
from .dbconn import Base

class UserData(Base):
    __tablename__ = 'user_data'

    id_ = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(128))
    access_level = Column(Integer, nullable=False)

    def __init__(self, name=None, password=None, access_level=None):
        self.name = name
        self.password = password
        self.access_level = access_level

    def __repr__(self):
        return '<User %r>' % (self.name)
