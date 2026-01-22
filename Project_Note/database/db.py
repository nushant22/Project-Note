from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pathlib import Path
from urllib.parse import quote


from dotenv import load_dotenv
env_file = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(env_file, override=True)


DATABASE_USER = "root"
DATABASE_PASSWORD = quote("C0dewithnush@nt") 
DATABASE_HOST = "127.0.0.1" 
DATABASE_PORT = "3306"
DATABASE_NAME = "project_note"

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

print(f"✓ Connecting to MySQL: {DATABASE_USER}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
