# Grouping Data

# .groupby()
# .groupby() splits your data into groups, then applies an aggregate method to each group separately.

(
    orders.groupby("cust_id")["total_order_cost"]
    .sum()
    .reset_index(name="total_spent")
)

# Q1. Group `techcorp_workforce` by department and count the employees in each.
import pandas as pd

techcorp_workforce.groupby("department")["id"].count()

# Note: 
# After .groupby().count(), the group column (department) becomes the DataFrame's index instead of a regular column. 
# .reset_index() moves it back to a normal column. 
# .reset_index(name="employee_count") turns the unnamed count into a descriptive column name. 

# like
import pandas as pd

techcorp_workforce.groupby("department")["id"].count().reset_index(name="employee_count")

# Note:
# Every .groupby() follows the same three-step pattern:

# Split: .groupby("column") — which column to group by
# Aggregate: .sum(), .mean(), .count(), etc. — what calculation to apply
# Reset: .reset_index() — clean up the output

# Q2. Group by department and calculate the sum and mean salary.
import pandas as pd

# Group by department, then aggregate salary
techcorp_workforce.groupby("department")["salary"].agg(["sum", "mean"]).reset_index(names="department")

# Important
# | Object Type	| .reset_index() Parameter | What does it name?	                        | Why is it named that way?
# | DataFrame	  | names                    | The column(s) created from the index.	    | Plural because a DataFrame index can have multiple levels (MultiIndex).
# | Series	    | name                     | The column created from the Series values.	| Singular because a Series only has one column of values to name.

# Sorting Grouped Results

# Q3. Count employees per department and sort by count, highest first.
import pandas as pd

# Count per department, then sort
df = techcorp_workforce.groupby("department")["id"].count().reset_index(name="employee_count")
df.sort_values("employee_count", ascending=False)

# Q4. Count the number of user events performed by MacBookPro users. Output the result along with the event name. Sort the result based on the event count in the descending order.
import pandas as pd

df = playbook_events[playbook_events["device"]=="macbook pro"].groupby("event_name")["user_id"].count().reset_index(name="event_count")
df.sort_values("event_count", ascending=False)

# Q5. Find how many times each artist appeared on the Spotify ranking list. Output the artist name along with the corresponding number of occurrences. 
# Order records by the number of occurrences in descending order.
import pandas as pd

spotify_worldwide_daily_song_ranking.groupby("artist")["position"].count().reset_index(name="list_count").sort_values("list_count", ascending=False)

# Q6. Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the top. 
# Sort your records by the number of times the song was in the top position in descending order.
import pandas as pd

df = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking["position"]==1].groupby("trackname")["position"]
    .count().reset_index(name="times_top1").sort_values("times_top1", ascending=False)
