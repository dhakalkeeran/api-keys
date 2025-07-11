import os
from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_api_key import generate_api_key, store_api_key
from verify_api_key import verify_api_key
from models import Base


def create_and_store_api_key(db, user_id=1):
    api_key, hashed_api_key = generate_api_key()
    store_api_key(db, user_id, hashed_api_key)
    logger.warning(f"{api_key} \nPlease note the API key. This is the only time you can see this key.")

def verify_incoming_api_key(db, incoming_api_key):
    verified = verify_api_key(db, incoming_api_key)
    if verified:
        print("Yay!! API key found.")
    else:
        logger.error("Sorry, API key not found !!")

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
    # create_and_store_api_key(db)
    
    # verify if the incoming API key is valid
    INCOMING_API_KEY = "DhtDCkE4pTRC0YgYmqnxlSqYs7XA9FHewbvfmO3Mkak"
    verify_incoming_api_key(db, INCOMING_API_KEY)

    db.close()

