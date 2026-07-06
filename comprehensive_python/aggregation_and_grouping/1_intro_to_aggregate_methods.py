# .count() and len(): How Many?
# len(df) = total rows in dataframe
# df.count = counts non null values per column

# Total rows
len(techcorp_workforce)

# Non-null values per column
techcorp_workforce.count()

# Non-null values in one column
techcorp_workforce["phone_number"].count()

# Unique values in a column
techcorp_workforce["department"].nunique()

# Note:
# len(df) counts all rows including NaN.
# .count() counts non-null values.
# .nunique() counts unique non-null values. 

# .sum(): Add It Up

# Q1. Calculate the total payroll by summing all salaries.
import pandas as pd

techcorp_workforce["salary"].sum()

# .sum() ignores NaN values by default.

# .mean(): The Average
# .mean() skips NaN values.

techcorp_workforce["salary"].mean()

# They work on text too — .min() gives you the first alphabetically, .max() gives the last. And on dates: .min() is the earliest, .max() is the most recent.

# Multiple Aggregates at Once with .agg()
# Pass a list of method names as strings. The result is a Series with one value per aggregation.

orders["total_order_cost"].agg(["sum", "mean", "min", "max"])

# Q2. Use `.agg()` to calculate the sum, mean, min, and max salary in one expression.
import pandas as pd

# Use .agg() with a list of method names
techcorp_workforce["salary"].agg(["sum", "mean", "min", "max"])

# Note: .describe() is just .agg() with a list of preset filters like count, mean, std, min, 25%, 50%, 75%, max. 

# Q3. What is the total sales revenue of Samantha and Lisa?
import pandas as pd

sales_performance[sales_performance["salesperson"].isin(["Samantha", "Lisa"])]["sales_revenue"].sum()

# Q4. Find the lowest, average, and the highest ages of athletes across all Olympics. HINT: If athlete participated in more than one 
# discipline at one Olympic games, consider it as a separate athlete, no need to remove such edge cases.
import pandas as pd

olympics_athletes_events["age"].agg(lowest_age="min", average_age="mean", highest_age="max").to_frame().T

# Q5. Find the hour with the highest gasoline cost. Assume there's only 1 hour with the highest gas cost.
import pandas as pd

lyft_rides[lyft_rides["gasoline_cost"] == lyft_rides["gasoline_cost"].max()][["hour"]]
