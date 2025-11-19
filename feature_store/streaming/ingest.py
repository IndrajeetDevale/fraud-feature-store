from datetime import datetime

from feature_store.online_store.store import update_user_features, get_user_features

REQUIRED_FIELDS = ["user_id", "amount", "event_type", "timestamp", "device_id"]

class EventValidationError(Exception):
    pass

def validate_event(raw_event):
    missing_fields = []

    for field in REQUIRED_FIELDS:
        if field not in raw_event:
            missing_fields.append(field)

    if missing_fields:
        raise EventValidationError(f"Missing required fields: {missing_fields}")
    
def normalize_event(raw_event):
    event = dict(raw_event)

    event["amount"] = float(event["amount"])

    ts = event["timestamp"].rstrip("Z")
    event["timestamp"] = datetime.fromisoformat(ts)

    return event

def process_event(raw_event):
    validate_event(raw_event)
    return normalize_event(raw_event)

def demo():
    sample_event = {
        "user_id": "u1",
        "amount": "120",
        "event_type": "payment",
        "timestamp": "2025-01-01T10:00:00Z",
        "device_id": "d1"
    }

    cleaned_event = process_event(sample_event)
    print("Cleaned event:")
    print(cleaned_event)

    features = update_user_features(cleaned_event)
    print("Updated online features for user:")
    print(features)

    fetched = get_user_features("u1")
    print("Fetched user features from online store:")
    print(fetched)

if __name__ == "__main__":
    demo()