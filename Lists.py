grades = [20,11,1]
grades.append(2000)
grades[2] = 67
grades.remove(20)
print (grades[0])
print (grades[2])
print (grades[-1])
print (len(grades))

for g in grades:
     print (g)

print(sum(grades))
print(max(grades))
print(min(grades))
print(f"{sum(grades)/len(grades ):.2f}")

print(grades[1:4])
print(grades[2:])
print(grades[:3])
