# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# 1. count
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

# 2. finding Index
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

# 3. Check
if apple_count < 5:
    print("apples needs to be restocked")
else:
    print("Apples are sufficiently stocked")

# 4. count
shelf = shelf.count("grapes")
if shelf < 1:
    print("Grapes need to be restocked")
else:
    print("Grapes are sufficiently stocked")

# 5. Check
if "oranges" in shelf:
orange_index = shelf_index("oranges")
    print("Oranges are at index:", orange_index)
else:
print("Oranges are out of stock.")
