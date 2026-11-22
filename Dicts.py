students =[ {
    "name" : "Abu",
    "age" : 22 , 
    "email" : "student04@gmail.com"
}]

students[0]["phone"] = "000000000"
while True:
   student = {}
   student["name"] = input("Enter your name: ")
   student["age"] = input("Enter your age: ")
   student["email"] =   input("Enter you email: ")
   student["phone"] = input("Enter your phone number: ")
   students.append(student)
   g = input("Do you want to continue ? (Yes/No)")
   if g.lower() == "no":
        break

print (students)
