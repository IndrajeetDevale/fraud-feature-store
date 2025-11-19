import pandas as pd

def load_events(csv_path):
    return pd.read_csv(csv_path)

def compute_user_aggregate_features(events_df):
    grouped = (
        events_df
        .groupby("user_id")
        .agg(
            transaction_count=("amount", "count"),
            total_amount=("amount", "sum"),
            avg_amount=("amount", "mean"),
        )
        .reset_index()
    )

    return grouped

def main():
    events = load_events("data/raw/events_sample.csv")

    features = compute_user_aggregate_features(events)

    print(features)

if __name__ == "__main__":
    main()