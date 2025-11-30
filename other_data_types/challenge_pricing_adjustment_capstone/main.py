# Create the dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# --- Check and update price of Eggs ---
category, price, stock = grocery_inventory["Eggs"]

if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price -= 1   # reduce price
else:
    print("The price of Eggs is reasonable.")

# save updated Eggs back into the dictionary
grocery_inventory["Eggs"] = (category, price, stock)

# --- Add Tomatoes ---
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# --- Manage stock of Milk ---
milk_category, milk_price, milk_stock = grocery_inventory["Milk"]

if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_stock += 20
else:
    print("Milk has sufficient stock.")

# save updated Milk back into the dictionary
grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock)

# --- Remove Apples if price is too high ---
apple_category, apple_price, apple_stock = grocery_inventory["Apples"]

if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

# --- Final print ---
print("Updated inventory:", grocery_inventory)
