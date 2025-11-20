# Fraud Feature Store

## Overview
Real-time fraud feature store built on AWS to support low-latency transaction risk scoring.

## Why this project
(TODO)

## High-level architecture
(TODO)

## Components
## End-to-End Flow (Current Status)

The system currently supports a minimal end-to-end feature store flow:

1. **Offline features (batch)**  
   - `feature_store/offline_store/offline_features.py` loads raw events from `data/raw/events_sample.csv`,
     aggregates per-user stats (transaction count, total amount, average amount), and writes a feature table to
     `data/offline/user_features.csv`.

2. **Streaming ingest (online path)**  
   - `feature_store/streaming/ingest.py` validates and normalizes incoming events
     (amount → float, timestamp → datetime).

3. **Online feature store (persistent)**  
   - `feature_store/online_store/store.py` maintains per-user online features such as `transaction_count`,
     `last_amount`, and `last_event_timestamp`, backed by `data/online/online_store.json` so state survives
     across runs.

4. **Feature serving**  
   - `feature_store/serving/api.py` demonstrates how a service can read the latest online features for a user,
     similar to a `GET /features/{user_id}` API backed by DynamoDB in production.


