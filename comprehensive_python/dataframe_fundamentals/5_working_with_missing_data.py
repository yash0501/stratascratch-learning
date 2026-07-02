# What NaN Actually Means
# NaN stands for "Not a Number," but it really means "missing" or "unknown."

# Note: In pandas, both NaN (from NumPy) and None (Python’s built-in) represent missing data. Pandas treats them interchangeably in most situations.

# Finding Missing Values: .isna()
# you can’t use == to check for NaN. Instead, use .isna():

fintech_app_users[fintech_app_users["phone_number"].isna()]

# .isna() returns True for every row where the value is missing, and False everywhere else.

# Q1. The product team is launching a new WhatsApp notification feature and needs to identify users who haven't provided their phone numbers yet. These users will be shown a prompt to add their contact information. Find all users who have not provided a phone number. Return the `user ID` and `name`.
import pandas as pd

data = fintech_app_users[fintech_app_users["phone_number"].isna()]
data[["user_id", "user_name"]]

# Excluding Missing Values: .notna()
# To find rows where a value exists, use .notna() — the opposite of .isna():

# Q2. Find all users who have a phone number on record.
import pandas as pd

fintech_app_users[fintech_app_users["phone_number"].notna()]

# Q3. Find wine varieties tasted by 'Roger Voss' and with a value in the 'region_1' column of the dataset. Output unique variety names only.
import pandas as pd

data = winemag_p2[(winemag_p2["region_1"].notna()) & (winemag_p2["taster_name"] == "Roger Voss")]
data[["variety"]].drop_duplicates()

# NaN Disappears from Both Sides of a Filter
# Filtering with == excludes NaN automatically
fintech_app_users[fintech_app_users["status"] == "active"]

# .str.contains(), .str.startswith(), and other .str methods return NaN (not False) for missing values. This means NaN rows are silently dropped from your filter results.

# Note: If you need to keep them, fill missing values first with .fillna() or combine your filter with .isna().

# Counting Missing Values

# Count NaN values per column
fintech_app_users.isna().sum()

# Percentage missing per column
fintech_app_users.isna().mean() * 100

# Total rows with any NaN
fintech_app_users.isna().any(axis=1).sum()

# Note: .isna().sum() counts missing values in each column.
# Note: .isna().mean() gives you the proportion.
# These are the first things to run when exploring a new dataset.

# Handling Missing Values with .fillna()

# Replace NaN in a specific column and keep the DataFrame
fintech_app_users["phone_number"] = (
    fintech_app_users["phone_number"].fillna("No phone")
)

# Q4. Replace missing phone number values in `fintech_app_users` with the text Unknown.
import pandas as pd

fintech_app_users["phone_number"].fillna("Unknown")

# Dropping Missing Values with .dropna()
# .dropna() removes rows that contain any NaN:

# Drop rows where ANY column is NaN
fintech_app_users.dropna()

# Drop rows where a SPECIFIC column is NaN
fintech_app_users.dropna(subset=["phone_number"])

# Q5. Remove all rows from `fintech_app_users` where the phone number is missing, then display the user ID and name.
import pandas as pd

fintech_app_users = fintech_app_users.dropna(subset=["phone_number"])
fintech_app_users[["user_id", "user_name"]]
