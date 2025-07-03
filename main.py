import os
from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_api_key import generate_api_key, store_api_key
from schema import Base


def create_and_store_api_key(db):
    api_key, hashed_api_key = generate_api_key()
    store_api_key(db, 1, hashed_api_key)
    logger.warning(f"{api_key} \nPlease note the API key. This is the only time you can see this key.")

if __name__ == "__main__":
    load_dotenv()

    USERNAME = os.environ.get("MYSQL_SERVER_USERNAME")
    PASSWORD = os.environ.get("MYSQL_SERVER_PASSWORD")
    
    if not (USERNAME and PASSWORD):
        logger.error("Could not find username or password!!")
        exit(1)

    DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost:3306/api_keys"
    
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # create and store the hashed API key in database
    create_and_store_api_key(db)

    db.close()

