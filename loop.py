# 🔋 Mobile Charging System
"""
battery_percentage = 10

while battery_percentage <= 100:
    print("Battery : ", battery_percentage ,"%")

    battery_percentage += 10
else:
    print("🔋 Charging Complete")

# Water Tank Filling

water_tank = 0
motor_on = 20

while water_tank <= 100:
    print("Tank : ", water_tank , "Liters")
    water_tank += 20
else:
    print("🚰 Tank Full")



# ATM PIN Login

original_pin = 1234


while True:
     atm_pin = int(input("Enter Your Pin : "))
     if atm_pin == original_pin:
          print("Login Successfull")
          break
     else :
          print("Invalid PIN")




# 🔐 Password Login System

original_password = 1234

while True:
    correct_pin = int(input("Enter Your Password : "))
    if correct_pin == original_password:
        print("✅ Login Successful ")
        break
    else:
        print("❌ Wrong Password")

    

# 🍫 Chocolate Distribution

teacher = 10

for teacher in range(1, 10 , 2):
    print(teacher)

for employee_id in range(101 , 111 , 1):
    print("Employee ID : ", employee_id , "-> Bonous Credit.")

# Bus Seat Numbers

for bus_seat_number in range (2, 20, 2):
    print("🪑 Seat :", bus_seat_number, "-> Booked")


for student_roll_numbers in range (3 , 31 , 3):
    print("🏃 Roll No: ", student_roll_numbers , "-> Selected")


for number in range(1, 31):

    if number % 5 == 0:
        print("⭐", number, "-> Special Number")
    else:
        print(number, "-> Normal Number")
    
for roll_number in range (1, 31):

    if roll_number % 2 == 0:
        print("✅ Roll No: ", roll_number , "-> Pass")
    else:
        print("❌ Roll No: ",roll_number , "-> Fail")


for employee_id in range (1001 , 1021):

    if employee_id % 2 == 0:
        print("✅ Employee ID:", employee_id ,  "→ Bonus Approved")
    else:
        print("⏳ Employee ID:", employee_id ,  "→ Bonus Pending")
"""

# 🎯 Problem – Cinema Ticket Discount

for seat_number in range(1,31):
    if seat_number % 5 ==0:
         print("🎁Seat: ",seat_number,"→ Free Popcorn" )
    elif seat_number % 2 ==0:
        print("💺 Seat: ",seat_number,"→ Premium Seat")
    else:
        print("🪑Seat: ",seat_number,"→ Regular Seat")