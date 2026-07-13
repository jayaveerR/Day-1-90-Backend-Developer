"""

original_pin = 1234
entered_pin = int(input("Enter Pin : "))

balance = 12000
withdraw = 790

acount_active =False

if acount_active:
    if original_pin == entered_pin:
        print("✅ Login Successful")
        if balance >= withdraw:
              print("✅ Transaction Successful\n Remaining Balance", balance -withdraw)
        else :
              print("❌ Insufficient Balance")
    else :
     print("invalid Pin")
else :
    print("🚫 Account Block")




wallet = 15000
product_price = 100

stock_available = True
is_prime_member = False

cupon = "SAVE500"
enterd_cupon = input("Enter Coupon : ")

if stock_available:
    if wallet >= product_price:
        print("✅ Payment Successful")
    
        if cupon == enterd_cupon:
            print("🎉 Coupon Applied")
            if is_prime_member:
                print("🚚 Free Delivery")
            else:
                print("🚚 Delivery Charge ₹99")
        else:
            print("⚠️ Invalid Coupon")
        print("📦 Order Placed Successfully")
    else:
        print("❌ Insufficient Balance")
else:
    print("🚫 Out Of Stock")


age = 70
oxygen = 85
insurance = True

if oxygen < 90:
    print("🚑 Emergency ICU")
elif age >= 60:
    print("👴 Senior Citizen Ward")
    if insurance:
        print("💳 Cashless Treatment")
    else:
        print("💵 Pay ₹10,000 Advance")
elif age >= 18:
    print("🧑 General Ward")
    if insurance:
        print("💳 Cashless Treatment")
    else:
        print("💵 Pay ₹5,000 Advance")
else:
    print("👶 Children Ward")

experience = 6
rating = 4.8
salary = 65000
department = "IT"

if experience < 2:
    print("❌ Promotion Not Eligible")
elif rating >= 4.5:
     print("🌟 Excellent Performance")
     if salary < 70000:
       print("💰 Salary Increased")
     else:
      print("💰 No Salary Change")
elif rating >= 3.5:
    print("👍 Good Performance")
    if department =="IT":
      print("📚 Advanced Training")
    else:
      print("📚 Basic Training")

else :
 print("⚠️ Performance Improvement Plan")

movies_list = ["Pushpa", "Dhee", "Salar"]
movie_name  = input("Enter Movie : ")
seats = True

balance = 50
movie_ticket = 100
premium = False

if movie_name in movies_list :
    print("✅ Show Available")
    if seats:
        print("Available Seats")
        if balance >= movie_ticket:
            print("✅ Payment Successful")
            if premium :
                print("🍿 Free Popcorn")
            else:
                print("🍿 Popcorn Costs ₹250")
            print("🎟️ Ticket Booked Successfully")
        else:
            print("❌ Insufficient Balance")
    else:
        print("❌ Seats Not Available")
else:
    print("❌ Show Not Available")

# 🎓 Student Result System

marks = 20
if marks >= 90:
    print("🌟 Grade A")
elif 75<= marks <=89 :
    print("🥈 Grade B")
elif 50<= marks <=74:
    print("🥉 Grade C")
elif 35<= marks <=49:
    print("✅ Pass")
else:
    print("❌ Fail")



# 🎓 College Exam Eligibility

attedence = 80
fee_paid = False

if attedence >= 75 and fee_paid:
    print("✅ Eligible for Exam")
elif attedence < 75:
    print("Low Attedence")
else:
    print("❌ Fees Not Paid")

"""

# 🛒 Online Shopping Discount System

customer_premium = False
purchase_amount = 500
cupon = False

if customer_premium and purchase_amount >= 5000:
    print("🎉 20% Discount Applied")
elif 3000 <= purchase_amount <=4999:
    print("🎁 10% Discount Applied")
    if cupon:
        print("🏷️ Extra ₹500 Discount")
    else :
        print("⚠️ No Extra Discount")
elif 1000 <= purchase_amount <=2999:
    print("🎁 5% Discount Applied")
else:
    print("❌ No Discount Available")