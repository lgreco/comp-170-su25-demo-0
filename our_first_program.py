
print("Hello Kofi, welcome to COMP 271.")
print("Hello Richard, welcome to COMP 271.")
print("Hello Lillie, welcome to COMP 170.")
print("Hello Heather, welcome to COMP 170.")
print("Hello Ben, wellco to COMp 177")

# Pattern: 
# "Hello" first_name ", welcome to " course_code

def personalized_greeting(name, course_code):
    print(f"Hello {name}, welcome to {course_code} !!!")

personalized_greeting("Cesar", "COMP 170")
personalized_greeting("Lula", "COMP 170")

print()


students = ["Omar", "Lula", "Enrique", "Arhub", "Ben", "Richard", "Heather"]
your_course = "COMP 170"

for name in students:
    personalized_greeting(name, your_course)
