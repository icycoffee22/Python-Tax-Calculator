section = ["Section 1", "Section 2", "Section 3", "Section 4"]

print("What is your Grade Level?")
gradeLevel = int(input())

if gradeLevel == 1:
    print("Your section is", section[0])
elif gradeLevel == 2:
    print("Your section is", section[1])
elif gradeLevel == 3:
    print("Your section is", section[2])
elif gradeLevel == 4:
    print("Your section is", section[3])
else:
    print("Grade level not recognized. Please recheck")