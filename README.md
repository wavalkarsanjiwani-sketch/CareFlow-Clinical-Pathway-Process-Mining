# CareFlow: Clinical Pathway Process Mining

A healthcare analytics project that uses process mining to analyze
patient journeys and identify workflow bottlenecks.

## Week 1: Event Log Simulation

**Completed**
- Set up Python 3.13 and VS Code
- Wrote `week1_eventlog.py`, a basic happy-path patient journey simulator
- Generated a synthetic event log: 1,100 patients, 5,500 events
- Columns: `case_id`, `activity`, `timestamp`
- Flow: Registration > Triage > Consultation > Lab Test > Discharge
- Output saved to `event_log.csv`

**Note:** The data is synthetic (simulated), not real patient data.

## Next Steps
- Add variations (skipped and repeated steps)
- Clean and validate the data
- Process discovery with PM4Py
