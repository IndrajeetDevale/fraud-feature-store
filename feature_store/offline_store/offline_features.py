import pandas as pd
import os

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

def write_features(features_df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    features_df.to_csv(output_path, index=False)
    print(f"Wrote features to {output_path}")

def main():
    events = load_events("data/raw/events_sample.csv")

    features = compute_user_aggregate_features(events)

    print(features)

    output_path = "data/offline/user_features.csv"
    write_features(features, output_path)

if __name__ == "__main__":
    main()