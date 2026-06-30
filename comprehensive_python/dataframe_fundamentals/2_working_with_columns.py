import pandas as pd

# renaming columns
# to rename a column in data output display
cols = techcorp_workforce[['first_name', 'joining_date']]
cols.rename(columns = {
  'first_name': 'First name',
  'joining_date': 'Hire date'
})

# You pass a dictionary to the columns parameter: keys are old names, values are new names. Only the columns you list get renamed — everything else stays the same.

# Q1. Rename department to Team and salary to Annual Pay.
import pandas as pd

cols = techcorp_workforce[["department", "salary"]]
cols.rename(columns = {
    "department": "Team",
    "salary": "Annual Pay"
})

# Creating New Columns with Arithmetic
# assign to a new column name using standard math operators
techcorp_workforce["monthly_salary"] = techcorp_workforce["salary"] / 12

# Q2. Create a daily salary column by dividing salary by 365. Show first name, salary, and daily salary.
import pandas as pd

techcorp_workforce['daily_salary'] = techcorp_workforce['salary']/365
techcorp_workforce[['first_name', 'salary', 'daily_salary']]

# Q3. We already created the bonus column. Now add a second column called `salary_with_bonus` that adds the bonus to the original salary, and update the display to include it.
import pandas as pd

techcorp_workforce["bonus"] = techcorp_workforce["salary"] * 0.10
techcorp_workforce["salary_with_bonus"] = techcorp_workforce["salary"] + techcorp_workforce['bonus']
techcorp_workforce[["first_name", "salary", "bonus", "salary_with_bonus"]]

# Combining Text Columns
# You concatenate strings with the + operator
techcorp_workforce["full_name"] = (
    techcorp_workforce["first_name"] + " " + techcorp_workforce["last_name"]
)

# Q4. Create a label column combining first name and department in the format Alice (HR). Show label and salary.
import pandas as pd

techcorp_workforce['label'] = techcorp_workforce['first_name'] + ' (' + techcorp_workforce['department'] + ')'

techcorp_workforce[['label', 'salary']]

# Note: String Concatenation Only Works on Strings
# If one of the columns is numeric, the + operator will try to do math instead of concatenation. Convert to string first with .astype(str): df["id"].astype(str) + " - " + df["name"].

# Removing Duplicates
# drop_duplicates() method removes duplicate rows from your results.

# Q5. Update the selection to return only unique order details.
import pandas as pd

orders[["order_details"]].drop_duplicates()

# When you select multiple columns before calling drop_duplicates(), it removes rows where the entire combination is duplicated:

# Q6. Find the unique combinations of customer ID and order details from `orders`.
import pandas as pd

orders[["cust_id", "order_details"]].drop_duplicates()

# Q7. Select the facility name and score from `los_angeles_restaurant_health_inspections`, renaming score to inspection score.
import pandas as pd

cols = los_angeles_restaurant_health_inspections[["facility_name", "score"]]
cols.rename(columns = {"score": "inspection score"})

# Q8. Find all unique grades that appear in `los_angeles_restaurant_health_inspections`.
import pandas as pd

los_angeles_restaurant_health_inspections[["grade"]].drop_duplicates()



