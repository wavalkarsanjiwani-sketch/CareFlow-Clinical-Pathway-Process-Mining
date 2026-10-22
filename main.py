
import pandas as pd
from pathlib import Path

# Project paths
project_path = Path(__file__).resolve().parent.parent
file_path = project_path / "data" / "hospital_opd.csv"
output_path = project_path / "outputs" / "event_log.csv"

# Load dataset
df = pd.read_csv(file_path)

# Check required columns
required_columns = [
    "appointment_id",
    "appointment_start_datetime",
    "prescription_start_datetime",
    "lab_start_datetime",
    "imaging_start_datetime",
    "pharmacy_start_datetime"
]

missing_columns = [c for c in required_columns if c not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Convert timestamps
time_columns = [
    "appointment_start_datetime",
    "prescription_start_datetime",
    "lab_start_datetime",
    "imaging_start_datetime",
    "pharmacy_start_datetime"
]

for col in time_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Build event log
events = []

activity_columns = {
    "Appointment": "appointment_start_datetime",
    "Prescription": "prescription_start_datetime",
    "Lab": "lab_start_datetime",
    "Imaging": "imaging_start_datetime",
    "Pharmacy": "pharmacy_start_datetime"
}

for activity, time_col in activity_columns.items():
    temp = df[["appointment_id", time_col]].copy()
    temp.columns = ["case_id", "timestamp"]

    temp["activity"] = activity

    temp = temp.dropna(subset=["case_id", "timestamp"])
    events.append(temp)

# Combine events
event_log = pd.concat(events, ignore_index=True)

# Remove repeated copies of the same event
event_log = event_log.drop_duplicates(
    subset=["case_id", "activity", "timestamp"]
)

# Validate appointment vs prescription timing
appointment_time = df.set_index("appointment_id")[
    "appointment_start_datetime"
]

prescription_time = df.set_index("appointment_id")[
    "prescription_start_datetime"
]

timing_check = pd.DataFrame({
    "appointment_time": appointment_time,
    "prescription_time": prescription_time
})

timing_check = timing_check[
    ~timing_check.index.duplicated(keep="first")
]

timing_check["timing_flag"] = "OK"

timing_check.loc[
    timing_check["prescription_time"] <
    timing_check["appointment_time"],
    "timing_flag"
] = "Prescription before appointment"

timing_check.loc[
    timing_check["prescription_time"] >
    timing_check["appointment_time"] + pd.Timedelta(days=30),
    "timing_flag"
] = "Prescription over 30 days later"

flag_path = project_path / "outputs" / "timing_review.csv"
timing_check.to_csv(flag_path)

print("\nTiming review saved to:", flag_path)
print("\nTiming flags:")
print(timing_check["timing_flag"].value_counts())

# Sort events
event_log = event_log.sort_values(
    ["case_id", "timestamp", "activity"]
)

# Save
event_log = event_log[
    ["case_id", "activity", "timestamp"]
]

output_path.parent.mkdir(parents=True, exist_ok=True)
event_log.to_csv(output_path, index=False)

print("Event log created!")
print("Total events:", len(event_log))
print("Unique cases:", event_log["case_id"].nunique())
print("\nActivity counts:")
print(event_log["activity"].value_counts())
print("\nFirst 10 events:")
print(event_log.head(10).to_string(index=False))
print("\nSaved to:", output_path)
