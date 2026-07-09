

# Checks the condition first. If it is True, its block executes.
# If the previous if (or elif) condition is False, Python checks this condition. If it is True, this block executes.
# elif : if true ayithe check cheyyadu. if false ayinappude check chestundi.
# If all previous conditions are False, the else block executes.

"""
balance = 8000
withdraw = 9000
# remaning = 3000

if balance >= withdraw:
    print("✅ Transaction Successfull \n Remaining Balance", balance - withdraw)
else :
    print("insufficient Balance")



temparature = 48
has_fever = True

if temparature >= 38 and has_fever:
    print("🤒 High Fever \n Visit Doctor")
else :
    print("😊 Normal")

marks = 82
attedance = 74
medical_certificate = True

if attedance >= 75 :
    print("Eligible For Exam ")
elif attedance < 75 and medical_certificate:
    print("Eligible with Medical Approval")
else:
    print("Not eligible")

"""

original_username = "jayaveer"
original_password = "python123"
balance = 15000
withdraw = 789
entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

if original_username == entered_username and original_password == entered_password:
    print("✅ Success Open Account" )
    if balance >= withdraw:
        print("✅ Transaction Successful")
        print("Remaining Balance:", balance - withdraw)
    else:
        print("❌ Insufficient Balance")
elif original_username != entered_username:
    print("❗ Invalid User Name")
elif original_password != entered_password:
    print(" ❗Invalid Password")
else:
    print("❌ Insufficient Balance")