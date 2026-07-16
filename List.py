"""
movies = ["Pushpa", "pushpa-2", "Bahubali -1",  "Bahubali -2",  "Salaar"]

for movie in movies:
    print(movie, '\n', end='',)
print()

students = ["Ravi", "Ajay", "Kiran", "Vamsi", "Suresh"]
count = 1
for students in students:
        print('👨‍🎓 Student',count ,':' , students )
        count += 1
print()



contact = ['Ajay','Ravi','Kiran','Vamsi','Suresh' ]
count =1

for contacts in contact:
    print("📱 Contact", count , ':', contacts)
    count += 1
print()



phones = [
    "iPhone",
    "Samsung",
    "OnePlus",
    "Nothing",
    "Google Pixel"
]

for phone in phones:
    print('first Phone  :', phones[0])
    print('Second Phone :', phones[2])
    print('Last Phone   :', phones[4])
    break
print()



laptops = ["HP", "Dell", "Asus","Lenovo","Acer","Apple"]


print("💻 First Laptop       :", laptops[0])
print("💻 Second Laptop      :", laptops[-1])
print("💻 Second Last Laptop :", laptops[-2])

"""

# Pattern Logic

for row in range(1, 6):
    for col in range(1 , row + 1):
        print("*", end='')
    print()