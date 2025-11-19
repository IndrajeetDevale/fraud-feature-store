from datetime import datetime

ONLINE_FEATURES = {}

def update_user_features(event):
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

    return current

def get_user_features(user_id):
    return ONLINE_FEATURES.get(user_id)

