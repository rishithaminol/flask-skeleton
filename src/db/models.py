from sqlalchemy import Column, Integer, String, ForeignKey, Text
from .dbconn import Base

class UserData(Base):
    __tablename__ = 'user_data'

    id_ = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(128))
    access_level = Column(Integer, nullable=False)

    def __init__(self, id_=None, name=None, password=None, access_level=None):
        self.id_ = id_
        self.name = name
        self.password = password
        self.access_level = access_level

    def __repr__(self):
        return '<User %r>' % (self.name)

# Access levels
# -1 - For all
# 0 - Administrative privileges
# 1 - Normal user (Without admin endpoint access)
class AccessLevels(Base):
    __tablename__ = 'access_levels'

    id_ = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    access_level = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)

    def __init__(self, id_=None, name=None, access_level=None, description=None):
        self.id_ = id_
        self.name = name
        self.access_level = access_level
        self.description = description
