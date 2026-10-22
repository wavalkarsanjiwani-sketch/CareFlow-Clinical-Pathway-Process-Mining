
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Project paths
project_path = Path(__file__).resolve().parent.parent
file_path = project_path / "outputs" / "event_log.csv"
output_path = project_path / "outputs" / "process_map.png"

# Load event log
df = pd.read_csv(file_path)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort activities within each case
df = df.sort_values(["case_id", "timestamp", "activity"])

# Create activity sequences
sequences = df.groupby("case_id")["activity"].apply(list)

# Count directly-following activity pairs
transitions = {}

for sequence in sequences:
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i + 1])
        transitions[pair] = transitions.get(pair, 0) + 1

# Display transitions
print("Process transitions:")
for pair, count in sorted(
    transitions.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{pair[0]} -> {pair[1]}: {count}")

# Draw process map
if transitions:
    labels = [f"{a} -> {b}" for (a, b) in transitions]
    counts = list(transitions.values())

    plt.figure(figsize=(11, 6))
    plt.barh(labels, counts)
    plt.xlabel("Number of cases / transitions")
    plt.title("Clinical Pathway - Directly Following Activities")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()

    print("\nProcess map saved to:", output_path)
else:
    print("No transitions available.")
