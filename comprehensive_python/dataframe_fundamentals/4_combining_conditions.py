# Multiple Conditions

# & (AND): Both Conditions Must Be True
orders[(orders["order_details"] == "Coat") & (orders["total_order_cost"] > 100)]

# Q1. Filter `techcorp_workforce` to HR employees earning over 80000.
import pandas as pd

techcorp_workforce[(techcorp_workforce["department"] == "HR") & (techcorp_workforce["salary"] > 80000)]

# Chaining multiple conditions
# You can chain as many & conditions as you need:

# Q2. Find Admin employees earning at least 80,000 who joined after January 1, 2022.
import pandas as pd

techcorp_workforce[
    (techcorp_workforce["department"] == "Admin") &
    (techcorp_workforce["salary"] >= 80000) &
    (techcorp_workforce["joining_date"] > "2022-01-01")
]

# Q3. Find the inspection date and risk category (`pe_description`) of facilities named 'STREET CHURROS' that received a score below 95.
import pandas as pd

data = los_angeles_restaurant_health_inspections[(los_angeles_restaurant_health_inspections["facility_name"] == "STREET CHURROS") & (los_angeles_restaurant_health_inspections["score"] < 95)]
data[["activity_date", "pe_description"]]

# | (OR): Either Condition Can Be True

# Q4. Filter `techcorp_workforce` to employees in HR or Admin using |.
import pandas as pd

techcorp_workforce[(techcorp_workforce["department"] == "HR") | (techcorp_workforce["department"] == "Admin")]

# Q5. Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD. Output all details related to retrieved records.
import pandas as pd

lyft_drivers[(lyft_drivers["yearly_salary"]<=30000)|(lyft_drivers["yearly_salary"]>=70000)]

# Matching a List of Values with .isin()
# Instead of chaining multiple == comparisons with |, use .isin()

# Instead of this:
df[(df["dept"] == "HR") | (df["dept"] == "Admin")]

# Do this:
df[df["dept"].isin(["HR", "Admin"])]

# Q6. Filter `techcorp_workforce` to employees in HR and Admin using `.isin()`.
import pandas as pd

techcorp_workforce[techcorp_workforce["department"].isin(["HR", "Admin"])]

# # Exclude with ~
techcorp_workforce[
    ~techcorp_workforce["department"].isin(["HR", "Admin"])
]

# Q7. Find all athletes who were older than 40 years when they won either Bronze or Silver medals.
import pandas as pd

data = olympics_athletes_events[(olympics_athletes_events["age"]>40) & (olympics_athletes_events["medal"].isin(["Bronze", "Silver"]))]

data[["name"]]

# Q8. Filter `techcorp_workforce` to salaries between 80000 and 120000.
import pandas as pd

techcorp_workforce[techcorp_workforce["salary"].between(80000, 120000)]

# .between() Is Inclusive
# .between(80000, 120000) includes both endpoints.

# .between() with dates
techcorp_workforce[techcorp_workforce["joining_date"].between("2022-01-01", "2022-12-31")]

# Q9. Find all orders placed during March 2019.
import pandas as pd

orders[orders["order_date"].between("2019-03-01", "2019-03-31")]

# ~ (NOT): Exclude Matches
# ~ inverts a boolean condition. It gives you everything that doesn’t match.

# Everyone except Admin
techcorp_workforce[~(techcorp_workforce["department"] == "Admin")]

# This is equivalent to using !=:
techcorp_workforce[techcorp_workforce["department"] != "Admin"]

# Q10. Rewrite the filter to exclude HR employees using ~ instead of !=.
import pandas as pd

techcorp_workforce[~(techcorp_workforce["department"] == "HR")]

# Use Parentheses to Control Order
# When mixing different operators because of precedence

# Q11. Find employees in HR or Engineering who earn more than 80,000. Add parentheses to make sure the salary filter applies to both departments.
import pandas as pd

techcorp_workforce[
    ((techcorp_workforce["department"] == "HR") |
    (techcorp_workforce["department"] == "Engineering")) &
    (techcorp_workforce["salary"] > 80000)
]

# Q12. The HR team is reviewing compensation packages for employees in support functions. They want to identify high earners in the HR and Admin departments for a salary benchmarking study. Find all employees who earn more than $80,000 and work in either the HR or Admin department. Return `first name`, `last name`, `department`, and `salary`.
import pandas as pd

data = techcorp_workforce[(techcorp_workforce["salary"]>80000) & (techcorp_workforce["department"].isin(["HR", "Admin"]))]

data[["first_name", "last_name", "department", "salary"]]

# Break conditions into variables
is_hr = techcorp_workforce["department"] == "HR"
is_admin = techcorp_workforce["department"] == "Admin"
high_earner = techcorp_workforce["salary"] > 80000

techcorp_workforce[(is_hr | is_admin) & high_earner]

# Key Takeaways
# & requires all conditions to be true (AND).
# | requires at least one condition to be true (OR).
# ~ inverts a condition (NOT).
# Every condition must be wrapped in parentheses when combining with & or |.
# & is evaluated before | — use extra parentheses to control the order.
# Use & and |, never Python’s and and or, when filtering DataFrames.
# .isin([list]) matches multiple values; ~ inverts any filter.
# .between(low, high) filters inclusive ranges — works with numbers and dates.

