total_running = 5
total_running = total_running + 15
print(total_running)

max_weight = 20
max_weight = max_weight / 3
print(max_weight)

	

# This is what I was looking for:

# Rewrite the following statement to force this order: Divide 5 by 7. Then multiply that result by y. Then subtract 1.
# x = 5 / 7 * y - 1 # WRONG 
# x = ((5 / 7) * y) - 1 # CORRECT 

# Rewrite the following statement to force this order: Subtract 1 from y. Then multiply that result by 7 for a second result. Then divide 5 by this second result.
# x = 5 / (7 * (y - 1)) # CORRECT
# x = 5 / 7 * y - 1 # WRONG