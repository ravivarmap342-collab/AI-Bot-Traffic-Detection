
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)

# Human-like traffic
human_data = pd.DataFrame({
    "requests_per_second": np.random.uniform(1, 5, 100),
    "avg_time_gap_ms": np.random.uniform(500, 3000, 100),
    "unique_urls": np.random.randint(5, 30, 100),
    "repeated_request_ratio": np.random.uniform(0.0, 0.3, 100),
    "session_duration_sec": np.random.uniform(60, 600, 100),
    "label": 0
})

# Bot-like traffic
bot_data = pd.DataFrame({
    "requests_per_second": np.random.uniform(20, 60, 100),
    "avg_time_gap_ms": np.random.uniform(10, 100, 100),
    "unique_urls": np.random.randint(1, 10, 100),
    "repeated_request_ratio": np.random.uniform(0.7, 1.0, 100),
    "session_duration_sec": np.random.uniform(10, 180, 100),
    "label": 1
})

# Combine both datasets
dataset = pd.concat([human_data, bot_data], ignore_index=True)

# Shuffle the data
dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the dataset
dataset.to_csv("bot_traffic_dataset.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(dataset))
print(dataset.head())
