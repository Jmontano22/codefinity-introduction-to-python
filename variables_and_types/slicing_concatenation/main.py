grocery_items = "milk cheese bread apples oranges chicken"

# 1. Slice the items from the big string:
dairy1 = grocery_items [0:4] #milk
dairy2 = grocery_items [5:11] #cheese
bakery1 = grocery_items [12:17] #bread

# 2. Concatenate exactly as the test expects:
print("we have dairy and bakery items:" + dairy1 + "," + dairy2 + ",and " + bakery1 + " " + "in aisle 5")