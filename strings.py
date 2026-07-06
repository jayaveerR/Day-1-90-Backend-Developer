# indexing
"""
email = "jayaveer1639@gmail.com"
name = "Jayaveer"
password = "jayaveer123456"
print(name[0],name[-0])
print(password[0])


# string  slicing

name = "jayaveer"
email = "nani@gmail.com"

print(name[::-1])

# string length

name = "jayaveer"

print(len(name))

#string methods 

name = "jayaveer"
age = "NANI"
print(name .upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(age.swapcase())

# sreach methods 

name = "nani"
email = "nani@gmail.com"
print(name.find("jayaveer"))
print(name.count("jayaveer"))
print(name.replace("nani", "Nani"))

# String Concatenation 
first_name = "jayaveer"
second_name = "nani"
print(first_name + second_name)


# escpe charecters \n , \t - table , 
print("Name : Jayaveer\nAge : 22")
print("Name\tAge\tCity")
print("Jay\t22\tGuntur")

# double quotes

print("He said, \"Python is Easy\"")

# single quotes 

print('It\'s my laptop')

# \\ 
print("C:\\Users\\Jayaveer\\Desktop")

# \t return
print("Hello\rPython")

# create a student report

print("Name    : Jayaveer \nAge     : 22 \nBranch  : MCA \nCollege : DVR College")

username = "raju@gmail.com"

if "@" in username:
    print("Invalid Username")
else:
    print("Valid Username")


"""

email = "ramanadhamayaveer@gmail.com"

if "@gmail.com" in email:
 print("Valid Email")
else:
 print("Invalid Email")

password = "jayaveer"

if "python" not in password:
  print("Valid Password ")
else:
 print("Invalid Password")  