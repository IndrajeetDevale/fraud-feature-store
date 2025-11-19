# Fraud Feature Store

## Overview
Real-time fraud feature store built on AWS to support low-latency transaction risk scoring.

## Why this project
(TODO)

## High-level architecture
(TODO)

## Components
- Batch features
The module `feature_store/offline_store/offline_features.py` demonstrates offline feature computation:
it loads raw events from `data/raw/events_sample.csv`, aggregates them per user, and writes a feature table
to `data/offline/user_features.csv`.


- Streaming features
- Online feature store
- Feature serving API

