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
    
    
   
    



total_grade = 0
counter=0
while True:
    subject=(input("Insert the subject: "))
    if subject.lower()=="exit": 
        break
    grade = float(input("Insert your grade for  "+subject+":"))
    if grade<0 or grade>100:
        print("Error:Invalid grade")
    else:
        total_grade += grade
        counter += 1
if counter>0:
    average=total_grade/counter
    print(f"Your total grade is:  {average:.2f}")
    print(comment(average))
else:
    print("No grades were entered")
   