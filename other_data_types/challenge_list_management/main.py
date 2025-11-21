meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

deli_dept = [meat, cheese, condiment]

if meat[0] in meat and meat[2] < 100:
    meat[2] = 100 #update its quantity to 100.

seaonal_meat = ["Turkey", 4.50, 100, "Sliced"]

deli_dept.append(seaonal_meat)

deli_dept.remove(condiment)
deli_dept.sort()

print("Initial Deli List:", deli_dept)
print("Updated Deli List:", deli_dept)
