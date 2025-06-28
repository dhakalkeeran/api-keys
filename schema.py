from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class APIKey(Base):
    __tablename__ = 'api_keys_table'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    api_key_hash = Column(String(64), nullable=False)  # SHA-256 hash (64 hex characters)
    created_at = Column(DateTime, server_default=func.now())
    last_used_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)