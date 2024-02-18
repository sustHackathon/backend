from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

# sqlAlchemyDatabaseUrl = "postgresql://postgres:iam4yearsold@localhost/project"


sqlAlchemyDatabaseUrl = f"postgresql://{config.Settings.database_username}:{config.Settings.database_password}@{config.Settings.database_hostname}/sustHackathon"


engine = create_engine(sqlAlchemyDatabaseUrl)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
