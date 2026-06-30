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

































