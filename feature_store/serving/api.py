from feature_store.online_store.store import get_user_features

def get_features_for_user(user_id):
    return get_user_features(user_id)

def demo():
    user_id = "u1"
    features = get_features_for_user(user_id)

    if features is None:
        print(f"No features for user {user_id}")
    else:
        print(f"Features for user {user_id}:")
        print(features)

if __name__ == "__main__":
    demo()