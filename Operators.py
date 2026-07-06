# Operators 

# Module 1: Arithmetic Operators

"""
+ - addition
- - subraction
* - multiplication
/  - devision
%  - modulo devision
** - 


price = 500
quantity = 3

total = price * quantity

print(price % quantity)

account_balance = 75000

deposit = 15000

withdraw = 12000

electricity_bill = 3500

mobile_recharge = 499

family_members = 4

balance_after_deposit = account_balance + deposit 

balance_after_withdraw = balance_after_deposit - withdraw

balance_after_bill = balance_after_withdraw - mobile_recharge - electricity_bill

each_member_share = balance_after_bill / family_members

print("Initial Balance       :", account_balance)
print(" Deposit              :", deposit)
print("After Deposit         :", balance_after_deposit)
print("Withdraw              :", withdraw)
print("After Withdraw        :", balance_after_withdraw)
print("Electricity Bill      :", electricity_bill)
print("Mobile Recharge       :", mobile_recharge)
print("Final Balance         :", balance_after_bill)
print("Each Member Share     :", each_member_share)



mobile_price = 35000
earbuds_price = 2500
cover_price = 800

mobile_quantity = 1
earbuds_quantity = 2
cover_quantity = 3

gst = 18
discount = 5000
delivery_charge = 150

friends = 2


mobile_total = mobile_price * mobile_quantity
earbuds_total = earbuds_price * earbuds_quantity
cover_total = cover_price * cover_quantity
product_total = mobile_total + earbuds_total + cover_total
gst_amount = product_total * gst/100
bill_after_gst = product_total + gst_amount
bill_after_discount = bill_after_gst - discount
delivery_charges = bill_after_discount + delivery_charge
final_bill = delivery_charges / friends

print("Mobile Total        :", mobile_total)
print("Earbuds Total       :", earbuds_total)
print("Cover Total         :", cover_total)
print("Product Total       :", product_total)
print("Add GST             :", gst_amount)
print("Bill After Gst      :", bill_after_gst)
print("Discount            :", discount)
print("After Discount      :", bill_after_discount)
print("Delivery Charge     :", delivery_charge)
print("Total Charges       :", delivery_charges)
print("Final Bill Each Pay :", final_bill)


# Assignment Operators   , = , += , -= , *= , /= 


wallet = 2000
recharge =1000
shoes = 700
cashback = 200

# Recharge 1000
wallet += recharge

# Buy Shoes 700
wallet -= shoes
# Cashback 200
wallet += cashback
print(wallet)


wallet = 5000

salary = 25000

rent = 8000

food = 2500

petrol = 1500

bonus = 3000

wallet += salary

wallet -= rent

wallet -= food

wallet -= petrol

wallet += bonus

print("Initial Wallet :", 5000)
print("Salary Added   :", 25000)
print("After Salary   :", 30000)
print("Rent           :",8000)
print("Food           :",2500 )
print("Petrol         :",1500)
print("Bonus          :",3000)
print("Final Wallet   :",wallet )



# Comparison Operators  == equal to equal to , ( != ) Not Equal To , > (Greather Than) , < (Less Than) , >= ( Greather Than OR Equal ), (<=) less Than OR Equal 


balance = 25000
minimum_balance = 10000

age = 22

entered_pin = 1234
original_pin = 1234

print(balance >= minimum_balance)

print(age >= 18)
print(entered_pin == original_pin)
print(balance < 50000)

# Logical Operators " and " , "Or", "Not". 

balance = 5000
pin = True

print(balance >= 4000 and pin)

email = False
phone = True

print(email or phone)

is_login = True

print(not is_login)


balance = 15000

minimum_balance = 10000

pin_verified = True

print(balance >= minimum_balance and pin_verified)


# ✅ Logical Operators if, elif, else


age = 14
if (age >= 18):
    print("Eligible for vote")
else :
    print("Not eligible for vote")
    

wallet = 5000
withdraw = 1000
if(wallet >= withdraw):
    print("Withdraw Successful")
else:
    print("Insufficient Balance")


marks = 37
pass_marks = 35
if (marks >= pass_marks):
    print("Pass")
else:
    print("Fail")

    
age = 25

if(age >= 18):
    print("Eligible")
else:
    print("Not Eligible")


salary = 50001
if (salary > 50000):
  print("Bonus Eligible")
else:
  print("No Bonus")

  

wallet = 15000
withdraw = 10000
entered_pin = 1234
original_pin = 1234
if (wallet >= withdraw and entered_pin == original_pin):
    print("Transaction Sucessfull")
else:
    print("Transaction Failed")


marks = 50
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

"""

name = "jayaveer"
print(name.lower())
print(name.upper())
print(name.startswith(name))