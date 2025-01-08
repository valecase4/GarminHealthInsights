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

### **Step 4: Checking for Missing Values and Missing Timestamp"**
- **Objective**: Identify and quantify missing timestamps and null values for each dataset.
   - A complete dataset is expected to have 720 rows (timestamps recorded every 2 minutes for a 24-hour period).
- **Action Taken**:
   - Reindexed each dataset to ensure the presence of all expected timestamps.
   - Counted the total number of missing timestamps and null values for each file.
   - Summed missing timestamps and null values to calculate the total number of missing data points per file.

**Result**:
The analysis revealed two problematic datasets with a significant number of missing or null values:
    - `2024-12-25.csv`
    - `2024-12-27.csv`
    
    - For the dataset `2024-12-21.csv`, a high number of missing values was expected, as the device was set up in the afternoon.
    - All other datasets had a manageable or no amount of missing data.

### **Step 5: Filling Missing Values with Linear Interpolation**
- **Objective**: Address missing data by applying linear interpolation to fill in missing timestamps and null values in the `heart_rate` column.
- **Action Taken**:
     - Reindexed all datasets to ensure timestamps align with the expected 2-minute intervals across 24 hours.
     - Applied linear interpolation to the `heart_rate` column to fill in gaps caused by missing data.
- **Result**: Missing timestamps and null values were successfully filled in all datasets using linear interpolation.

All datasets now contain a complete range of timestamps and no null values, ready for further analysis.

### **Step 6: Verification of Data Types and Formats**
- **Objective**: Ensure that the `timestamp` column is in the correct format (hours:minutes) and that time intervals between
consecutive timestamps are consistently 2 minutes.
- **Action Taken**:
    - Added a new column, time_difference, to calculate the time interval between consecutive timestamps.
    - Verified that all intervals (excluding the first row) were equal to 2 minutes.
    - Applied the same verification process to all files in the dataset.
- **Result**: After applying the verification procedure to all files, it was confirmed that all intervals between
consecutive `timestamp` values are exactly 2 minutes.

### **Step 7: Identification and Removal of Outliers**
- **Objective**: Detect and handle outliers in the heart rate data to ensure the validity and reliability of the dataset for analysis.
- **Strategy**:  From analysis of Garmin Connect data, the highest heart rate recorded during exercise was 187 bpm. Therefore, any values greater than 224 bpm (20% higher than the maximum recorded value) were considered outliers. Considering the resting heart rate trends in Garmin Connect, values below 35 bpm were deemed biologically improbable and marked as outliers.
- **Action Taken**: 
    - Implemented a filter to identify values outside the range [35 bpm - 224 bpm] in each dataset.
    - Detected 1 outlier in the dataset with timestamp 23:24.
    - Removed the identified outlier and saved the updated dataset.
- **Results**: The dataset is now free from outliers based on the defined criteria. The modified dataset was successfully saved, ensuring consistency across all heart rate files.

### **Step 8: Duplicate Rows Check**
- **Objective**: Ensure there are no duplicate rows in each dataset based on the `timestamp` column.
- **Action Taken**: 
    - Checked each file for duplicate rows using the `timestamp` column as the unique identifier.
- **Results**: No duplicate rows were found in any of the files.