# Sorting with .sort_values()

# Ascending (default) — lowest first
orders.sort_values("total_order_cost")

# Descending — highest first
orders.sort_values("total_order_cost", ascending=False)

# Q1. Sort `techcorp_workforce` by `salary` from lowest to highest.
import pandas as pd

techcorp_workforce.sort_values("salary")

# Sorting Dates
# .sort_values work if the values are datetime type. if not, convert to datetime type by pd.to_datetime()

# Q2. Sort employees to show the most recently hired first.
import pandas as pd

techcorp_workforce.sort_values("joining_date", ascending=False)

# Sorting by Multiple Columns
orders.sort_values(
    ["cust_id", "total_order_cost"],
    ascending=[True, False]
)

# Q3. Sort `techcorp_workforce` by `department` ascending and `salary` descending.
import pandas as pd

techcorp_workforce.sort_values(["department", "salary"], ascending=[True, False])

# Filtering Then Sorting

# Q4. Find all orders with a total cost over 50 and sort them from most to least expensive.
import pandas as pd

orders[orders["total_order_cost"] > 50].sort_values("total_order_cost", ascending=False)

# Sorting by Computed Values

# Q5. Create a column with the length of each employee’s first name, then sort by it (longest first).
import pandas as pd

techcorp_workforce["name_len"] = techcorp_workforce["first_name"].str.len()
techcorp_workforce.sort_values("name_len", ascending=False)

# Limiting Results
# Use .head(), .tail() to get top n 

# Shortcuts: .nlargest() and .nsmallest()

# These are equivalent:
df.sort_values("salary", ascending=False).head(5)
df.nlargest(5, "salary")

# And these:
df.sort_values("salary").head(3)
df.nsmallest(3, "salary")

# Bottom-N with .nsmallest()

# Q6. Find the 3 lowest-paid employees.
import pandas as pd

techcorp_workforce.nsmallest(3, "salary")

# Q7. Find the 3 most expensive orders.
import pandas as pd

orders.nlargest(3, "total_order_cost")

# Q8. Find the 3 highest-value orders placed by customer 15.
import pandas as pd

orders[orders["cust_id"]==15].nlargest(3, "total_order_cost")

# In practice, you almost never sort alone. The real pattern is a chain: filter to the rows you care about, sort by the column that matters, 
# limit to the top N, and select only the columns you need. 

# Filter → Sort → Limit → Select columns
(
    df[df["department"] == "Engineering"]
    .sort_values("joining_date", ascending=False)
    .head(5)
    [["first_name", "last_name", "joining_date"]]
)

# Q9. Find the 5 most recently hired employees in the Engineering department. Show their first name, last name, and joining date.
import pandas as pd

techcorp_workforce[techcorp_workforce["department"] == "Engineering"].nlargest(5, "joining_date")[["first_name", "last_name", "joining_date"]]
