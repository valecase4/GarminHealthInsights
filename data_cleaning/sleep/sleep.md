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

### **Step 5: Identification of Null Values**
- **Objective:**  
  Ensure there are no missing (`NaN`) values in the datasets. 

- **Actions Taken:**  
  1. Checked for missing values (`NaN`) across all datasets.  

- **Results:**  
  - No datasets contained null values.

---

### **Step 6: Identification of Missing Time Slots**
- **Objective:**  
  Verify if the sleep stages datasets contain any missing time slots between `end_time` of one entry and `start_time` of the next. 

- **Actions Taken:**  
  1. Scanned all sleep stages datasets for missing time slots.  

- **Results:**  
  - No missing time slots were found.

---

### **Step 7: Completeness of Heart Rate Datasets**
- **Objective:**
  Assess the completeness of the heart rate datasets by comparing the expected number of entries (based on sleep duration) with the actual entries.

- **Actions Taken:**  
  1. Calculated the expected number of rows for each dataset based on sleep duration.
  2. Compared the expected rows with the actual rows for each file.

- **Results:**  
  - All heart rate datasets were found to be 100% complete.
  - However, datasets for `2024-12-21` and `2025-01-01` were completely missing and were removed from the analysis.

---

### **Step 8:  Identification of Outliers**
#### **Sleep Stages Datasets**
- **Objective:**
  Verify the presence of outliers in the sleep stages datasets.

- **Actions Taken:**  
  1. Checked all datasets for invalid sleep stage labels.

- **Results:**  
  -  No outliers detected. All datasets contained only valid labels: "Awake", "REM", "Deep", "Light".

#### **Nighttime Heart Rate Datasets**
- **Objective:**
  Verify the presence of outliers in nighttime heart rate datasets.

- **Actions Taken:**  
  1. Plotted boxplots to visualize the distribution of heart rate values.
  2. Plotted histograms with density curves to further analyze the data distribution and detect anomalies.

- **Results:**  
  -  No significant outliers detected. Heart rate values were consistent and followed a normal distribution pattern. The IQR method was not applied, as visual analysis showed no extreme deviations.

---

### **Step 9: Duplicate Check (Sleep Stages Datasets)**

**Objective:** Verify the integrity of the sleep stages datasets by identifying duplicate rows and overlapping time slots.

---

#### **9.1 Duplicate Rows**
- **Description:** Checked for rows with identical `start_time` and `end_time` values.
- **Methodology:** 
  - Iterated through all files in the dataset directory.
  - Identified rows where both `start_time` and `end_time` were exactly the same as another row in the file.
- **Result:**
  - No duplicate rows were found across all datasets.

---

#### **9.2 Overlapping Time Slots**
- **Description:** Verified if any time slots overlap or intersect between rows within each dataset.
- **Methodology:** 
  - Converted `start_time` and `end_time` to datetime format for precise temporal comparisons.
  - Sorted each dataset by `start_time`.
  - Checked if the `end_time` of a row was greater than the `start_time` of the next row.
- **Result:**
  - No overlapping or intersecting time slots were found across all datasets.


