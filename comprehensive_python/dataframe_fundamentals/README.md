### Section 1: Data Loading, Selection, & Inspection [Doc 1]

*   **Pandas Overview**: Pandas is used to manage structured data (CSV, Excel, JSON, SQL). Its core structure, the DataFrame, behaves like a spreadsheet.
*   **Loading Data**:
    ```python
    import pandas as pd
    df = pd.read_csv('data.csv')
    df = pd.read_excel('data.xls')
    df = pd.read_json('data.json')
    df = pd.read_sql("SELECT * FROM employees", connection)
    ```
*   **Selecting Columns**:
    *   Single column: `df['col_name']`
    *   Multiple columns: `df[['col1', 'col2']]`
*   **Viewing Data**:
    *   `df.head(n)`: Shows top *n* rows (default is 5).
    *   `df.tail(n)`: Shows bottom *n* rows.
*   **DataFrame Metadata and Diagnostics**:
    *   `df.shape`: Returns a tuple `(rows, columns)` indicating dimensions.
    *   `df.columns`: Lists all column names.
    *   `df.dtypes`: Shows the data type of each column.
    *   `df.info()`: Summarizes column names, non-null counts, data types, and memory usage.
    *   `df.describe()`: Provides a quick statistical summary (mean, std, min, percentiles, max) for numerical columns.

---

### Section 2: Renaming, Math, Text, & Duplicates [Doc 2]

*   **Renaming Columns**: 
    Use `.rename(columns={...})` with a dictionary mapping old names (keys) to new names (values). Unlisted columns remain unchanged.
    ```python
    df.rename(columns={'old_name': 'new_name'})
    ```
*   **Arithmetic Column Creation**: 
    Create new columns by applying mathematical operators to existing ones.
    ```python
    df['daily_salary'] = df['salary'] / 365
    ```
*   **Text Concatenation**: 
    Concatenate text columns using the `+` operator. 
    *   *Rule*: String concatenation only works on string types. If a column is numeric, convert it first using `.astype(str)`.
    ```python
    df['label'] = df['first_name'] + ' (' + df['department'] + ')'
    df['id_str'] = df['id'].astype(str) + " - " + df['name']
    ```
*   **Removing Duplicates**: 
    Use `.drop_duplicates()` to remove redundant entries. 
    *   When applied to a single column selection, it returns unique values in that column.
    *   When applied to multiple selected columns, it removes rows where the entire combined row values are identical.
    ```python
    df[['cust_id', 'order_details']].drop_duplicates()
    ```

---

### Section 3: Basic Filtering & String Matching [Doc 3]

*   **Boolean Indexing (Masking)**: 
    Filtering is performed by creating a boolean (True/False) series and passing it inside the DataFrame brackets.
    ```python
    mask = df['department'] == 'HR'
    df[mask]  # Or directly: df[df['department'] == 'HR']
    ```
*   **Comparison Operators**: Use standard operators (`>`, `<`, `>=`, `<=`, `!=`) to filter numbers.
*   **Date Filtering**: If a column has proper datetime formatting, standard comparison operators evaluate chronologically.
    ```python
    df[df['joining_date'] > '2021-12-31']
    ```
*   **Excluding Values**: Use `!=` to drop specific records.
*   **String Matching with `.str` Accessor**:
    *   `df[df['col'].str.startswith("Prefix")]`
    *   `df[df['col'].str.endswith(".suffix")]`
    *   `df[df['col'].str.contains("substring")]`
    *   Case-insensitive search: Combine `.str.lower()` with `.str.contains()`, or use `case=False` argument inside `.str.contains()`.
    ```python
    df[df['name'].str.lower().str.contains("john")]
    # Or
    df[df['name'].str.contains("john", case=False)]
    ```

---

### Section 4: Advanced Logic & Compound Conditions [Doc 4]

*   **Logical AND (`&`) and OR (`|`)**:
    *   `&` requires both conditions to be True.
    *   `|` requires at least one condition to be True.
*   **Precedence & Syntax Rules**:
    1.  **Always** wrap each individual condition in parentheses.
    2.  Use the symbols `&` and `|`. Never use Python’s built-in `and` or `or` for filtering Pandas DataFrames.
    3.  Because `&` takes evaluation priority over `|`, use extra outer parentheses to control complex combinations.
    ```python
    df[((df['dept'] == 'HR') | (df['dept'] == 'Admin')) & (df['salary'] > 80000)]
    ```
*   **Matching List Elements (`.isin()`)**: 
    Instead of chaining multiple `|` statements, check if column values match a list.
    ```python
    df[df['department'].isin(['HR', 'Admin'])]
    ```
*   **Range Filtering (`.between()`)**: 
    Checks if a number or date falls within a specific range. It is **inclusive** of both endpoints.
    ```python
    df[df['salary'].between(80000, 120000)]
    ```
*   **Logical NOT (`~`)**: 
    Inverts any boolean filter to exclude matches.
    ```python
    df[~df['department'].isin(['HR', 'Admin'])]  # Excludes HR and Admin
    ```
*   **Variables for Readability**: Complex logic can be broken down into individual boolean masks:
    ```python
    is_hr = df['department'] == 'HR'
    high_earner = df['salary'] > 80000
    df[is_hr & high_earner]
    ```

---

### Section 5: Handling Missing Data (NaN) [Doc 5]

*   **Understanding NaN**: 
    `NaN` (Not a Number) represents missing or unknown data. Pandas treats `NaN` (NumPy) and `None` (Python) interchangeably.
*   **Identifying and Excluding Missing Values**:
    *   Do not use `== NaN` to check for missing values. Instead, use `.isna()`.
    *   To find complete, non-missing values, use `.notna()`.
    ```python
    df[df['phone'].isna()]   # Missing numbers
    df[df['phone'].notna()]  # Exists in record
    ```
*   **The NaN Dropout Effect**: 
    Comparisons like `==` and `.str` methods silently exclude `NaN` rows because they do not yield a definitive True/False evaluation. To prevent this, fill missing values first or explicitly combine the expression with `.isna()`.
*   **Quantifying Missing Values**:
    *   `df.isna().sum()`: Counts missing values in each column.
    *   `df.isna().mean() * 100`: Calculates the percentage of missing values per column.
    *   `df.isna().any(axis=1).sum()`: Identifies the number of rows containing at least one missing value.
*   **Filling Missing Values**: 
    Use `.fillna('default_val')` to replace missing values.
    ```python
    df['phone_number'] = df['phone_number'].fillna("Unknown")
    ```
*   **Dropping Missing Values**:
    *   `df.dropna()`: Drops rows if *any* column contains a NaN value.
    *   `df.dropna(subset=['col_name'])`: Drops rows only if a NaN value is present in the specified columns.

---

### Section 6: Sorting & Limiting Data [Doc 6]

*   **Sorting Values**: Use `.sort_values("column_name")`.
    *   Default is ascending. Pass `ascending=False` for descending order.
    *   *Dates*: Sorting chronologically requires the column to be a datetime type. If it is stored as a string, use `pd.to_datetime()` before sorting.
*   **Sorting Multiple Columns**: 
    Pass a list of column names and a matching list of boolean values to specify individual sort directions.
    ```python
    df.sort_values(['dept', 'salary'], ascending=[True, False])
    ```
*   **Sorting by Computed Columns**: 
    You can sort by values calculated on the fly, such as string length.
    ```python
    df['name_len'] = df['first_name'].str.len()
    df.sort_values('name_len', ascending=False)
    ```
*   **Top-N and Bottom-N Extraction**:
    *   Use `.head(n)` or `.tail(n)` after sorting to isolate records.
    *   *Shortcuts*: Use `.nlargest(n, 'col')` and `.nsmallest(n, 'col')` to replace combinations of sorting and head limits.
    ```python
    df.sort_values('salary', ascending=False).head(5)  # Identical to:
    df.nlargest(5, 'salary')
    ```
*   **Method Chaining syntax**: 
    Wrap expressions in parentheses to chain filtering, sorting, limiting, and selecting columns across multiple lines:
    ```python
    (
        df[df['department'] == 'Engineering']
        .sort_values('joining_date', ascending=False)
        .head(5)
        [['first_name', 'last_name', 'joining_date']]
    )
    ```
