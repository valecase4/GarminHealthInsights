# Data Cleaning Log: Activities Dataset

## 1. Introduction
**Dataset:** Activities  
**Objective:** Clean and explore the dataset to ensure data consistency and quality for further analysis.

---

## 2. Data Overview
**Initial Data Structure:**  
- Rows: 18  
- Columns: 2 (`date`, `activity (Y/N)`)  
- Date Range: 2024-12-21 to 2025-01-07  

---

## 3. Checks Performed
**Checks Performed:**  
1. **Null or Missing Values:**  
   - No missing values detected.  
2. **Date Range Completeness:**  
   - No missing dates detected.
3. **Data Types and Formats:**  
   - `date` column: Converted to datetime format.  
   - `activity (Y/N)` column: Contains only 'Yes'/'No' values.
5. **Duplicate Entries:**  
   - No duplicate dates found.  

---

## 4. Final Data Overview
**Final Data Structure:**  
- Rows: 17
- Columns: 2 (`date`, `activity (Y/N)`)  
- Date Range: 2024-12-21 to 2025-01-06  

---

## 6. Notes/Considerations
**Notes:**  
1. Rows with a `date` value after 2025-01-06 has been removed.
