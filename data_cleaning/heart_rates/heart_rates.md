# Data Cleaning Log: Heart Rates Dataset

## 1. Introduction
**Dataset:** Heart Rates  
**Objective:** Clean and validate the dataset to ensure consistency and prepare it for further analysis. The dataset consists of daily files (`.csv`), each containing timestamps and heart rate values.

---

## 2. Workflow Summary
The following steps were performed as part of the data cleaning process:

### **Step 1: File Filtering**
- **Objective:** Include only the `.csv` files within the date range `2024-12-21` to `2025-01-06`.
- **Action Taken:**  
  - Filtered all files based on their names, ensuring they represent valid dates in the specified range.  
  - Files beyond the limit date `2025-01-06` were excluded.  

**Result:**  
A total of **17 files** were included in the range.  

---

### **Step 2: Sample Dataset Verification**
- **Objective:** Verify the structure of a sample file to ensure it contains the expected columns.  
- **Action Taken:**  
  - Loaded a random file from the filtered list.
  - Confirmed the presence of the following columns:
    - `timestamp`: Records the time of each heart rate measurement.
    - `heart_rate`: Records the heart rate value (in bpm).

**Result:**  
The sample file has the expected structure.

### **Step 3: All Datasets Verification**
- **Objective**: Verify that all the other files have the same structure (consistency)

- **Action Taken:**  
  - Loaded and validated all files, checking for: Presence of the `timestamp` and `heart_rate` columns.  

**Result**:
All the files have the same structure.