# NaN in Aggregations

# How Each Method Handles NaN

# len() counts ALL rows, including NaN
len(techcorp_workforce)

# .count() counts only non-null values
techcorp_workforce["phone_number"].count()

# .sum(), .mean(), .min(), .max() all skip NaN
techcorp_workforce["salary"].mean()

# Q1. Calculate what fraction of employees have a phone number on record.
import pandas as pd

# Count non-null phones, then divide by total rows
techcorp_workforce["phone_number"].count()/len(techcorp_workforce)

# Q2. The data quality team is auditing employee records to assess the completeness of contact information. Calculate and return the ratio of employees who have a `NULL` phone number.
import pandas as pd

(len(techcorp_workforce) - techcorp_workforce["phone_number"].count())/len(techcorp_workforce)

# NaN in GROUP BY
# If department has NaN values, those rows are excluded
(
    techcorp_workforce
    .groupby("department")["id"]
    .count()
    .reset_index(name="emp_count")
)

# All aggregate methods skip NaN by default.
# len(df) counts all rows; .count() counts non-null only.
# The gap between them tells you how much data is missing.
# .fillna(0) before aggregating treats missing as zero.
# .groupby() silently drops NaN group keys.
