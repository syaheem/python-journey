def comment(score):
    if score == 100:
        return"I gave u easy question that's why"
    elif score >= 80:
        return "You're okay,not as smart as me,but okay"
    elif score>= 60:
        return"You're an NPC boy"
    elif score >= 40:
        return"You're very lucky ma boii"
    elif score >= 20:
        return"You almost fail miserably"
    elif score > 0:
        return "You fail miserably"
    else:
        return "You dont even try"
    
    
   
    

subjects = []

total_grade = 0
counter=0
while True:
    subject = {}
    subject["name"]=(input("Insert the subject: "))
    if subject["name"].lower()=="exit": 
        break
    subject["grade"] = float(input("Insert your grade for  "+ subject["name"] +":"))
    if subject["grade"] <0 or subject["grade"] >100:
        print("Error:Invalid grade")
    else:
        total_grade += subject["grade"]
        counter += 1
        subjects.append(subject)
    
if counter>0:
    average=total_grade/counter
    print(f"Your average grade is:  {average:.2f}")
    print(comment(average))
    highest = subjects[0]
    for s in subjects:
        if s["grade"]>highest["grade"]:
            highest = s
    
else:
    print("No grades were entered")
for subject in subjects:
    print(f"{subject['name']}  -> {subject['grade']:.2f}")
