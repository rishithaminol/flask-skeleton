from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from src.db.dbconn import Base
from sqlalchemy.dialects.postgresql import INET
import datetime

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

class SessionData(Base):
    __tablename__ = 'session_data'

    id_ = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(UserData.id_), unique=False, nullable=False)
    user_agent = Column(Text, nullable=True, unique=False)
    ip = Column(INET, nullable=False, unique=False)
    time = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    expire = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    session_id = Column(String(128), unique=True, nullable=False)

    def __init__(self, id_=None, id_user=None, user_agent=None,
                        ip=None, time=None, expire=None, session_id=None):
        self.id_ = id_
        self.id_user = id_user
        self.user_agent = user_agent
        self.ip = ip
        self.time = time # the time user logged in
        self.expire = expire
        self.session_id = session_id # User session id generated by flask-login module
