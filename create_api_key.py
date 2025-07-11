import secrets
import json
import hashlib
from loguru import logger
from models import APIKey

def hash_api_key(api_key):
    return hashlib.sha256(api_key.encode()).hexdigest()

def generate_api_key(key_length=32):
    """
    Generates an API key.

    Args:
        key_length (int): Length of each API key.

    Returns:
        key: Generated API key.
        hash: Hashed API key.
    """
    api_key = secrets.token_urlsafe(key_length)
    hashed_api_key = hash_api_key(api_key)
    return api_key, hashed_api_key

def generate_api_keys(num_keys=1, key_length=32, restrictions=None):
    """
    Generate API keys with optional restrictions.

    Args:
        num_keys (int): Number of keys to generate.
        key_length (int): Length of each API key.
        restrictions (dict): Dictionary of restrictions to assign to keys.

    Returns:
        keys: A dictionary of hashed API keys and their associated restrictions.
        hash: A dictionary of API keys and its hashed counterpart
    """
    keys = {}
    hashed_keys = {}
    for _ in range(num_keys):
        key, hashed_key = generate_api_key(key_length)
        
        # Assign restrictions if provided
        keys[hashed_key] = restrictions if restrictions else {}
        hashed_keys[key] = hashed_key

    return keys, hashed_keys

def store_api_key(db, user_id, hashed_api_key):
    new_key = APIKey(user_id=user_id, api_key_hash=hashed_api_key)
    db.add(new_key)
    db.commit()
    db.refresh(new_key)

def save_keys_to_file(keys, filename="api_keys.json"):
    """
    Save API keys to a file in JSON format.

    Args:
        keys (dict): API keys and their restrictions.
        filename (str): File name to save the keys.
    """
    with open(filename, "w") as file:
        json.dump(keys, file, indent=4)
    logger.info(f"API keys saved to {filename}")

if __name__ == "__main__":
    # Define restrictions (optional)
    restrictions = {
        "usage_limit": 1000,  # Max API calls
        "valid_until": "2025-12-31"  # Expiration date
    }

    api_keys, hashed_api_keys = generate_api_keys(num_keys=1, key_length=40, restrictions=restrictions)

    save_keys_to_file(api_keys)
    logger.info(f"Generated API Keys: {api_keys}")
    logger.info(f"Hashed API Keys: {hashed_api_keys}")