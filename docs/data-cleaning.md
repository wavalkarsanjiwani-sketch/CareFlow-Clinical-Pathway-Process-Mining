# CareFlow – Hospital OPD Data Cleaning & Preprocessing

## 1. Project Overview

CareFlow is a Clinical Pathway Process Mining project focused on understanding patient appointment and prescription workflows in a hospital OPD environment.

The purpose of data cleaning is to prepare a structured, consistent, and analysis-ready dataset for process mining, event log generation, and Power BI visualizations.

Data preparation was performed using Microsoft Excel and Power Query.

## 2. Objectives of Data Cleaning

The main objectives were:

- Improve data quality and consistency.
- Identify missing values and potential duplicate records.
- Prepare date and time columns for chronological analysis.
- Standardize column names and data types where required.
- Prepare data for event log generation.
- Make the dataset suitable for Power BI reporting and process analysis.

## 3. Dataset Overview

**Dataset:** Hospital OPD Dataset  
**Initial dataset size:** 62,422 records and 24 columns  
**Tools used:** Microsoft Excel, Power Query, Power BI

Important fields used in the project include:

- `patient_id`
- `appointment_id`
- `appointment_start_clean`
- `prescription_start_clean`
- `prescription_end_datetime_clean`
- `flow_name`

The cleaned dataset contains appointment and prescription-related information used for the initial process analysis.

## 4. Data Cleaning Process

### 4.1 Data Inspection

The dataset was inspected before beginning the cleaning process.

The inspection focused on:

- Understanding column names and their meanings.
- Reviewing available appointment and prescription fields.
- Identifying date/time columns.
- Checking data types and data completeness.
- Understanding which fields are relevant to the project.

### 4.2 Missing Values Analysis

Missing values are important in healthcare workflow analysis because not every patient necessarily follows the same activities.

The following checks are relevant:

- Identifying blank or null values.
- Reviewing missing values in important identifiers.
- Checking appointment timestamp completeness.
- Checking prescription timestamp completeness.
- Reviewing optional activity fields, where available.

**Handling approach:**

- Missing values should be evaluated according to their meaning.
- Optional activity timestamps should not automatically be treated as errors.
- Critical identifiers and timestamps should be investigated before excluding records.
- Missing values should not be filled with arbitrary dates or identifiers.

Exact missing-value counts and final treatment decisions will be documented after validation.

### 4.3 Duplicate Records Analysis

Duplicate records can affect event counts and process analysis.

The duplicate review should distinguish between:

- Exact duplicate rows.
- Repeated appointment IDs.
- Repeated patient IDs.
- Repeated activities and timestamps.

A patient may have multiple appointments, and an appointment may contain multiple legitimate workflow events.

Therefore, repeated patient IDs are not automatically considered duplicates.

The initial dataset inspection did not identify exact duplicate rows.

Further checks should be based on the appropriate business key and event definition.

### 4.4 Date and Time Cleaning

Date/time fields are essential for reconstructing the clinical workflow.

The project uses cleaned timestamp fields, including:

- `appointment_start_clean`
- `prescription_start_clean`
- `prescription_end_datetime_clean`

Cleaning and preparation activities included:

- Preparing cleaned prescription datetime columns.
- Reviewing the cleaned date/time values.
- Using the cleaned timestamp fields for chronological event analysis.
- Preparing the timestamps for Power BI and event log processing.

Date/time values must be validated for missing values, invalid formats, and unexpected event order.

### 4.5 Column Preparation

The dataset was prepared for analysis by selecting relevant fields for the initial workflow.

The initial event log focuses on:

- Appointment
- Prescription Started
- Prescription Ended

The original prescription datetime columns were removed from the prepared Power Query output after their cleaned versions were created.

Only fields required for the intended analysis should be retained in the final analytical dataset.

### 4.6 Power Query Transformations

Microsoft Power Query was used to prepare the dataset.

The preparation workflow included:

1. Loading the dataset.
2. Inspecting the available columns.
3. Preparing cleaned datetime fields.
4. Reviewing the transformed data.
5. Applying the transformations using **Close & Apply**.
6. Loading the prepared data into Power BI.

The exact transformation sequence can be verified through Power Query Applied Steps.

## 5. Event Log Preparation

The prepared data is used to create an event log for process analysis.

The initial event log includes:

- Case identifier
- Activity name
- Event timestamp

The event log represents the initial appointment and prescription workflow.

Events are sorted chronologically to support process map generation.

The current event log is an initial workflow representation and does not claim to capture every possible clinical activity.

## 6. Data Quality Considerations

The following checks are important before final analysis:

- Confirm required identifiers are available.
- Validate timestamp formats.
- Review missing values in required fields.
- Investigate duplicate events.
- Review unexpected event sequences.
- Avoid removing legitimate repeated appointments or activities.
- Protect potentially identifiable healthcare information.

## 7. Privacy and Data Protection

Healthcare-related datasets may contain sensitive information.

Before publishing project files:

- Check for patient names and contact information.
- Review patient and appointment identifiers.
- Avoid publishing identifiable patient-level records.
- Prefer synthetic, anonymized, or appropriately de-identified sample data.
- Review generated event logs and screenshots before uploading.

A dataset should not be considered anonymous solely because names or contact information are absent.

## 8. Tools and Technologies

- Microsoft Excel
- Power Query
- Microsoft Power BI
- Python
- Pandas
- Matplotlib
- GitHub

## 9. Future Improvements

- Add a missing-value summary report.
- Add automated duplicate validation.
- Validate event ordering.
- Add data quality metrics.
- Expand the event log when additional validated activity timestamps become available.
- Develop the final Power BI dashboard.
- Improve project documentation and reproducibility.

## 10. Conclusion

Data cleaning and preprocessing provide the foundation for the CareFlow project.

The prepared dataset supports the initial event log and process map generation. Further validation and dashboard development will improve the reliability and interpretability of the project.
