"""
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

students = ["Ravi", "Jay", "Sai"]

for student in students:
    print(student)

customers = ["Jayaveer", "Nikhitha", "Raju"]
for customer in customers:
    print("WellCome To Bisonix", customer)
    
# start , stop , step
for u in range(10 , 20 , 4):
 print(u)

for i in range(10, 0, -1):
    print(i)

# nested loop

for i in range(2):
   for j in range(4):
      print(i , j)

for classroom in range(1,4):
   print("class", classroom)

   for student in range(1,4):
    print("Students", student)

customers = ["Jayaveer", "Ravi", "Nani", "Sai"]

for customer in customers:
    if customer == "Ravi":
       break
    print(customer)

students = ["Jay", "Ravi", "Sai"]

for student in students:

    if student == "Ravi":
        continue

    print(student)

# break  , Continue
customers = ["Jayaveer", "Ravi", "Nani", "Sai"]

for customer in customers:
    if customer == "Ravi":
        continue
        break
    print(customer)

"""
# Pass While-Loop

