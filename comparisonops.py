
#Let's talk a little more about ==. It's a type of comparison operator, specifically it's
#the equality operator. As you learned in the last chapter, you use it to compare two
#things to see if they're equal.
#You can use the equality operator to compare a variable with a string, a
#variable with a number, a variable with a math expression, or a variable with a
#variable. And you can use the equality operator to compare various
#combinations. All of the following are legal first lines in if statements:

if full_name == "Mark" + " " + "Myers":
if full_name == first_name + " " + "Myers":
if full_name == first_name + " " + last_name:
if total_cost == 81.50 + 135:
if total_cost == materials_cost + 135:
if total_cost == materials_cost + labor_cost:
if x + y == a - b: