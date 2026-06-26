
cost_per_hour = 0.51

# per day cost
per_day = cost_per_hour * 24

# per week cost
per_week = per_day * 7

# per month cost (30 days)
per_month = per_day * 30

# days with $918
days = 918 / per_day

print("Cost to operate one server per day: $", per_day)
print("Cost to operate one server per week: $", per_week)
print("Cost to operate one server per month: $", per_month)
print("Number of days server can run with $918:", days)
