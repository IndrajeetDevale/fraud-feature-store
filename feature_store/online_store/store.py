from datetime import datetime
from .sqlite_store import init_db, write_features, read_features

init_db()

def update_user_features(user_id, event):
    existing = read_features(user_id) or {
        "transaction_count": 0,
        "last_amount": 0.0,
        "last_event_timestamp": None
    }

    last_device_id = existing.get("last_device_id")
    device_changed = (last_device_id is not None and last_device_id != event["device_id"])


    current_count = existing.get("transaction_count") or 0
    current_count += 1


    last_ts_str = existing.get("last_event_timestamp")
    if last_ts_str:
        last_ts = datetime.fromisoformat(last_ts_str)
    else:
        last_ts = None

    timestamp = event["timestamp"]

    if last_ts:
        time_delta = (timestamp - last_ts).total_seconds()
    else:
        time_delta = None

    high_velocity_flag = (time_delta is not None and time_delta < 30)


    if isinstance(timestamp, datetime):
        ts_str = timestamp.isoformat()
    else:
        ts_str = str(timestamp)


    features = {
        "transaction_count": current_count,
        "last_amount": float(event["amount"]),
        "last_event_timestamp": ts_str,
        "last_device_id": event["device_id"],
        "device_changed": device_changed,
        "time_since_last_event": time_delta,
        "high_velocity_flag": high_velocity_flag
    }



    write_features(user_id, features)
    return features

def get_user_features(user_id):
    return read_features(user_id)