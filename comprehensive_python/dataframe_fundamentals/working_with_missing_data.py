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

