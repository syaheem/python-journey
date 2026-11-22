students =[ {
    "name" : "Syaheem",
    "age" : 22 , 
    "email" : "syaheem04@gmail.com"
}]

students[0]["phone"] = "0196832580"
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