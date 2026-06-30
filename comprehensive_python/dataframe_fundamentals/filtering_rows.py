#  Filtering rows

# Boolean indexing
# Filtering in pandas works by creating a True/False mask and passing it inside brackets. Every row where the condition is True stays; everything else is dropped.

import pandas as pd

mask = df[department] == "HR"
df[mask]

# or
df[df[department] == "HR"]

# Filtering text values
orders[orders["order_details"=="Coat"]]

# Q1. Find all inspection details made for facilities owned by 'GLASSELL COFFEE SHOP LLC'.

import pandas as pd

los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections["owner_name"]=="GLASSELL COFFEE SHOP LLC"]

# Comparison operators
# Filtering numbers

# Q2. Find employees earning more than 100,000. Display their first name, last name, and salary.
import pandas as pd

rows = techcorp_workforce[techcorp_workforce["salary"] > 100000]
rows[["first_name", "last_name", "salary"]]

# Filtering dates
# As long as the column is a proper datetime type, comparison operators work chronologically.

# Q3. Find employees who joined after January 1, 2022.
import pandas as pd

techcorp_workforce[techcorp_workforce["joining_date"]>'2021-12-31']

# Excluding Values with !=
# != is the simplest way to exclude a single value from your results.

# Q4. Find all employees who are not in the Admin department.
import pandas as pd

techcorp_workforce[techcorp_workforce["department"]!="Admin"]

# String Matching with .str

# Starts with
df[df[name].str.startswith("Jo")]

# Contains
df[df[name].str.contains("john")]

# ends with
df[df[name].str.endswith(".com")]

# case-insensitive
df[df[name].str.lower().str.contains("john")]

# Q5. Filter `orders` to rows where order details start with the letter B.
import pandas as pd

orders[orders["order_details"].str.startswith("B")]

# Q6. Find all employees whose first name contains the letter 'o' anywhere.
import pandas as pd

techcorp_workforce[techcorp_workforce["first_name"].str.lower().str.contains("o")]

# Q7. Find all files from the table whose filename starts with 'draft' and whose contents contain the word 'optimism'. Output all columns.
import pandas as pd

google_file_store[(google_file_store["contents"].str.contains("Optimism", case = False)) & (google_file_store["filename"].str.contains("draft", case = False))]




