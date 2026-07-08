"""# variables in python - store data using Names


name='jayaveer'
age=20
print(name,age)


# Module 2: Variable Declaration

name='jayaveer'
age=23
salary=50000
print(name,age,salary)

# Module 3: Variable Naming Rules

salary
name
age


# Data Types

# integer
age = 20

#float
age = 20.5

# Boolean
is_login =  True
is_logout = False

#string

name = "jayaveer"

# None 

user = None

# Module-5 Type()

name = 'jayaveer'
print(type(name))

# Module-6 Multiple Variables

a,b,c=10,20,30
print(a,b,c)

# Module 7: Same Value
x=y=z=100
print(x,y,z)

# Module 8: Variable Reassignment

age = 115
age = 5
age = 1
print(age)

# Module 9: Dynamic Typing
x = 10
x = "Python"
x = True
x = 56
print(type(x))

# Module 10: Input()

name = input("Enter Your Name ")


# Module 11: Casting
age = int(input("Enter Age "))


# Module 12: print()
# print(name)

# Module 13: f-string
name = "Jayaveer i Am From Mangalagiri " 
print(f"My Name is {name}")

# Module 14: Memory Concept
x=10
y=x
print(x)

# Module 15: id()

x = 0
print(id(x))

# Module 16: Constants
PI=3.14

# Commits


Hii
Hello World!

# Module 18: Keywords

import keyword

print(keyword.kwlist)

# Module 19: Variable Scope (Introduction)

name = "Jay"

# Module 20: Best Practices
student_name 



🧠 Interview Questions
Variable ante enti?
Python lo datatype declare cheyyala?
Dynamic typing ante enti?
type() use enti?
id() use enti?
input() return type enti?
int() enduku use chestam?
None ante enti?
True and False datatype enti?
Python naming conventions enti?


#------------------------------------------------------------------------------------------------------------------------------------------------------

# Declare Variables 
student_name = "Jayaveer"
student_age = 20
student_branch = "MCA"
student_college= "DVR&Dr.Hs Mic College Of Technology"
student_cgpa = 8.5
student_fee = 350000
student_email = "ramanadhamjayaveer@gmail.com"
student_Phone = 7995232673 
student_passed = True

print("Name    :", student_name)
print("age     :",student_age)
print("branch  :",student_branch)
print("College :", student_college)
print("CGPA    :", student_cgpa)
print("Fee     :", student_fee)
print("Email   :", student_email)
print("Phone   :", student_Phone)
print("passed  :", student_passed)


# variable Declare + print()

employee_name = "jayaveer"
employee_id = 25
employee_department = "MCA"
employee_salary = 25000
employee_email = "ramanadhamjayaveer@gmail.com"
employee_phone = " 7995232673 "
employee_city = "Mangalagiri"
employee_is_active = True

print("Employee Name :", employee_name)
print("Employee ID :", employee_id)
print("Department :", employee_department)
print("Salary :", employee_salary)
print("Email :", employee_email)
print("Phone :", employee_phone)
print("City :", employee_city)
print("Active Employee :", employee_is_active)


is_login = True
print(is_login)
is_login = False
print(is_login)


customer_name = "Jayaveer"
mobile_name  = "Vivo-Y21"
mobile_price = 25000
discount     = 35
gst          = 15
final_Price  = 15000
is_paid      = True

print("customer Name :", customer_name)
print("mobile Name   :", mobile_name )
print("Mobile Price  :", mobile_price)
print("Discount      :", discount , "%")
print("Gst           :", gst , "%")
print("Final_price   :", final_Price)
print("Paid          :", is_paid)

print(type(customer_name))
print(type(mobile_name))
print(type(mobile_price))



# Amazon 

product_name = "Remote control car"

product_id = 2544798559954

product_price = 50000

product_quantity = 15

product_rating = 3.5

product_brand = "Bisonix"

product_category = "Toys"

is_available = True

is_returnable = False


print("Product Name    :",  product_name)
print("Product ID      :", product_id)
print("Product Price   :", product_price)
print("Product Quantity:", product_quantity)
print("Product Rating  :", product_rating,"⭐⭐⭐")
print("Product Brand   :", product_brand)
print("Product Category:", product_category)
print("Available       :", is_available)
print("Return Product  :", is_returnable)

print(type(product_name))
print(type(product_id))
print(type(product_price))
print(type(product_quantity))
print(type(product_rating))
print(type(product_brand))
print(type(product_category))
print(type(is_available))
print(type(is_returnable))




#------------------------------------------------------

patient_name = "Jayaveer"

patient_id = 245596145

patient_age = 25

patient_gender = "Male"

patient_blood_group = "B-"

patient_weight = 55

patient_height = 5.5

doctor_name = "Mr.Sai Kumar Reddy"

hospital_name = "Arshini Hospital"

room_number = 2445

treatment_fee = 25000

is_admitted = True

is_insurance_available = False

print("Patient Name          :", patient_name)
print("Patient Id            :", patient_id)
print("Patient Age           :", patient_age)
print("Patient Gender        :", patient_gender)
print("Patient Blood Group   :", patient_blood_group ,"🩸")
print("Patient Weight        :", patient_weight , "KG")
print("Patient Height        :", patient_height , "ft")
print("Doctor Name           :", doctor_name, "🧑‍⚕️")
print("Hospital Name         :", hospital_name , "🏥")
print("Room Number           :", room_number,)
print("Treatment Fee         :", treatment_fee , "💵")
print("Admitted              :", is_admitted)
print("Insurance Available   :", is_insurance_available)

print(type(patient_name))
print(type(patient_id))
print(type(patient_age))
print(type(patient_gender))
print(type(patient_blood_group))
print(type(patient_weight))
print(type(patient_height))
print(type(doctor_name))
print(type(hospital_name))
print(type(room_number))
print(type(treatment_fee))
print(type(is_admitted))
print(type(is_insurance_available))

"""

name , city , age = "Jayaveer", "Mangalagiri", 25

print(name , city , age)


# same value 
saving_balance = current_balance = loan_balance = 0
print(saving_balance , current_balance , loan_balance)

age = int(input("Enter Age "))

name = "jayaveer"
age  = 20
city = "Mangalagiri"

print(f"My name is{name} , Age is {age}, Your City {city}")



subscription = True
internet = False
if subscription == internet:
    print("Movie Start")
print("Cannot play Movie")

username =input("Enter Your Name : ")
password =input("Enter Your Password : ")

if username in "jayaveer":
    print("Invalid Username")
elif password in "python123":
    print("Invalid Password")
else:
    print("invalid password")