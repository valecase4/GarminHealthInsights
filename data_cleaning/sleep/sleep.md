# Data Cleaning Log: Sleep Dataset

## 1. Introduction
**Datasets:**  
1. Heart rate during sleep.  
2. Sleep stages based on time intervals.  

**Objective:**  
Clean and integrate the two types of datasets to produce a unified dataset for each day with the columns:
- `timestamp`: Records the time of the measurement.  
- `heart_rate`: Records the heart rate value during sleep.  
- `sleep_stage`: Indicates the sleep stage during the time interval.

---

## 2. Workflow Summary

### **Step 1: Sample Dataset Verification**
- **Objective:**  
  Verify the structure and contents of both dataset types using sample files.

- **Actions Taken:**  
  1. Loaded a sample file from the heart rate dataset.  
  2. Loaded a sample file from the sleep stages dataset.  
  3. Used the `.head()` method to inspect the first 5 rows of each dataset.

- **Results:**  
  - The sleep stages dataset was correctly structured.  
  - The heart rate dataset had an issue: the columns `timestamp` and `heart_rate` were inverted.

---

### **Step 2: Define Expected Output**
- **Objective:**  
  Determine the desired structure of the final cleaned datasets.  

- **Actions Taken:**  
  1. Defined the expected output: for each day, a dataset with the columns:
     - `timestamp`
     - `heart_rate`
     - `sleep_stage`
  2. The final dataset for each day will be obtained by intersecting the two datasets (heart rate and sleep stages) based on `timestamp`.

---

### **Step 3: Filter Files by Date Range**
- **Objective:**  
  Retain only files within the valid date range: `2024-12-21` to `2025-01-06`.  

- **Actions Taken:**  
  1. Iterated through all files in the directory.
  2. Excluded files with dates outside the valid range.

- **Results:**  
  - All files outside the specified range were successfully removed.

---

### **Step 4: Resolve Column Inversion**
- **Objective:**  
  Correct the column inversion issue in the heart rate dataset.  

- **Actions Taken:**  
  1. Renamed the columns `timestamp` and `heart_rate` to their correct positions.  

- **Results:**  
  - The issue was resolved, and the datasets are now properly structured.

---

