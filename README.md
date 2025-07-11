# api-keys

This repository contains scripts and utilities for secure **API key generation, storage, and verification**. It provides a simple yet robust system to manage API keys with hashing and database integration.

## Features
- 🔑 **API Key Generation** — Secure random API keys using Python's `secrets` module.
- 🔒 **API Key Hashing (SHA-256)** — API keys are hashed before storing in the database for security.
- 🗄️ **Database Storage** — Store hashed API keys in a relational database using SQLAlchemy ORM.
- ✅ **API Key Verification** — Verify incoming API keys by comparing hashes.


## Setup

### 1. Clone the Repository
```
git clone https://github.com/dhakalkeeran/api-keys.git
cd api-keys
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Configure Database
Update the DATABASE_URL in your Python script:

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/api_keys"
```
```
CREATE DATABASE api_keys;
```
### 4. Create Tables
Run this snippet once to create required tables:

```
from sqlalchemy import create_engine
from models import Base

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
```

## Usage
### Generate and Store an API Key
```
from create_api_key import generate_api_key, store_api_key

api_key, hashed_api_key = generate_api_key()
store_api_key(db, user_id, hashed_api_key)
```

### Verify an Incoming API Key
```
from verify_api_key import verify_api_key

verified = verify_api_key(db, incoming_api_key)
```

## Technologies Used
```
Python 3.10.12
SQLAlchemy
PyMySQL
MySQL
SHA-256 (hashlib)
```
Details on [requirements.txt](requirements.txt).

## To-Do
<ul>
  <li>Add API key rotation functionality.</li>
  <li>Add expiry mechanism for API keys.</li>
  <li>Dockerize the entire project for easy deployment.</li>
</ul>
