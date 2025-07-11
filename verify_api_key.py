from sqlalchemy import func
from create_api_key import hash_api_key
from models import APIKey


def verify_api_key(db, incoming_api_key):
    incoming_hash = hash_api_key(incoming_api_key)

    key_record = db.query(APIKey).filter(
        APIKey.api_key_hash == incoming_hash,
        APIKey.is_active == True
    ).first()

    if key_record:
        # Update last_used_at for tracking usage
        key_record.last_used_at = func.now()
        db.commit()
        return True
    else:
        return False