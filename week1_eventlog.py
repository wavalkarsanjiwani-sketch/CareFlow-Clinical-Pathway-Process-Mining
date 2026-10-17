import pandas as pd
import random
from datetime import datetime, timedelta

activities = ["Registration", "Triage", "Consultation", "Lab Test", "Discharge"]
rows = []

for i in range(1, 1101):
    case_id = f"P{i:03d}"
    time = datetime(2026, 10, 1, 8, 0) + timedelta(minutes=random.randint(0, 600))
    for act in activities:
        rows.append([case_id, act, time])
        time += timedelta(minutes=random.randint(5, 60))

df = pd.DataFrame(rows, columns=["case_id", "activity", "timestamp"])
df.to_csv("data/event_log.csv", index=False)
print(df.head(10))
print("Total rows:", len(df))