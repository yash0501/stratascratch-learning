# Filtering Groups
# You can't do both grouping and filtering simultaneously in a same query. It needs to be joined (chained) together.

# Filtering After Grouping
order_counts = (
    orders.groupby("cust_id")["id"]
    .count()
    .reset_index(name="order_count")
)
order_counts[order_counts["order_count"] >= 3]

# Q1. Group `techcorp_workforce` by department, count employees, and keep only departments with 3 or more.
import pandas as pd

df = techcorp_workforce.groupby("department")["id"].count().reset_index(name="employee_count")
df[df["employee_count"]>3]

# Group, aggregate into a new DataFrame, then filter it like any other DataFrame.

# Q2. Filter to recent hires first, then find departments with more than 2 of those hires.
import pandas as pd

# Step 1: filter rows to recent hires
recent = techcorp_workforce[
    techcorp_workforce["joining_date"] > "2022-01-01"
]

# Step 2: group and count
data = recent.groupby("department")["id"].count().reset_index(name="employee_in_dept")
# Step 3: filter groups with > 2
data[data["employee_in_dept"]>2]

# Q3. Find departments with more than 2 employees and an average salary over 75,000.
import pandas as pd

# Group, aggregate, then filter on two conditions
data = techcorp_workforce.groupby("department").agg(emp_count=("id", "count"), emp_salary=("salary", "mean")).reset_index()
data[(data["emp_count"]>2) & (data["emp_salary"]>75000)]

# Q4. Find departments with at more than or equal 5 employees.
import pandas as pd

data = employee.groupby(["department"])["id"].nunique().to_frame("count").reset_index()
data[data["count"]>5][["department"]]
