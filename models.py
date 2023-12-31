from atexit import register

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "postgres"
DB_PASSWORD = "13241234"
DB_HOST = "localhost"
DB_PORT = 5432
DB_DB = "DB_Flask"

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
register(lambda: engine.dispose())
Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    creation_data = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)


Base.metadata.create_all()
