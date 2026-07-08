# 1. Initialization (Start Value)

# 2. Condition

# 3. Update
"""
count = 1 # initialization

while count <= 15:   #condition
    print(3 * count)
    count += 1     #update

attempt = 2

while attempt <= 3:
    print("Loggin Attempt", attempt)
    attempt += 1

battery = 100

while battery >= 0:
    print("battery percentage until it reaches ", battery,"%")
    battery -= 10


balance = 10000
withdraw = 2000
# remaining  = 8000

while balance >=0:
     print("Current Balance :", balance)
     balance -= 2000
     

balance = 600
withdraw = 300

while balance >= withdraw:
    balance -= withdraw
    print("✅ Transaction Successful")
    print("Current Balance:", balance)

if balance < withdraw:
    print("❌ Insufficient Balance")

    

age = 14
  
if age >= 18:
 print("Eligible")
print("noo")



wallet = 1000
payment = 200
# remaining = 150

if wallet >= payment:
    print("Payment Successfull")
else:
  print("Insuffiecient Balance")
subscription = True
internet = True

if subscription == internet:
    print("Movie Start")
else:
    print("Cannot play Movie")

"""
original_username = "jayaveer"
original_password = "jayaveer@123"

username = input("Enter Your Username : ")
password = input("Enter Your Password : ")

if original_username == username and original_password == password :
    print("✅ Login SuccussFull")
if username != original_username and password != original_password:
    print("Invalid username password")
elif username != original_username:
    print(" ❌Invalid Username")
elif password != original_password:
    print("❌Invalid Password")