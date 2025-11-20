from datetime import datetime
import json
import os
from typing import Dict, Any

STORE_PATH = "data/online/online_store.json"

ONLINE_FEATURES: Dict[str, Dict[str, Any]] = {}

def _serialize_timestamp(value):
    if isinstance(value, datetime):
        return value.isoformat()
    return value

def _deserialize_timestamp(value):
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            return value
    
    return value

def _load_store():
    if not os.path.exists(STORE_PATH):
        return {}
    
    with open(STORE_PATH, "r") as f:
        raw = json.load(f)
    
    store = {}

    for user_id, features in raw.items():
        fixed = {}
        for key, value in features.items():
            if key.endswith("_timestamp"):
                fixed[key] = _deserialize_timestamp(value)
            else:
                fixed[key] = value
        store[user_id] = fixed
    
    return store

def _save_store(store):
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)

    to_write = {}

    for user_id, features in store.items():
        fixed = {}
        for key, value in features.items():
            if isinstance(value, datetime):
                fixed[key] = _serialize_timestamp(value)
            else:
                fixed[key] = value
        to_write[user_id] = fixed

    with open(STORE_PATH, "w") as f:
        json.dump(to_write, f, indent=2)

def update_user_features(event):
    global ONLINE_FEATURES

    if not ONLINE_FEATURES:
        ONLINE_FEATURES = _load_store()


    user_id = event["user_id"]
    amount = event["amount"]
    timestamp = event["timestamp"]

    current = ONLINE_FEATURES.get(user_id, {
        "transaction_count": 0,
        "last_amount": 0.0,
        "last_event_timestamp": None
    })

    current["transaction_count"] += 1

    current["last_amount"] = amount
    current["last_event_timestamp"] = timestamp

    ONLINE_FEATURES[user_id] = current

    _save_store(ONLINE_FEATURES)

    return current

def get_user_features(user_id):
    global ONLINE_FEATURES

    if not ONLINE_FEATURES:
        ONLINE_FEATURES = _load_store()

    return ONLINE_FEATURES.get(user_id)

