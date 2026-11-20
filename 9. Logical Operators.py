Name = input("Enter your name: ")
# if Name == "ALICE" or Name == "BOB":
#     print("welcome to sliderin, " + Name + "!")
# elif Name == "HARRY" or Name == "DAVID":
#     print("welcome to grifender, " + Name + "!")  
# else:
#     print("Sorry, you are not allowed to enter the club.")

#MARKS = int(input("Enter your marks: "))
# if MARKS >= 90 and MARKS <= 100:
#     print("You got an A grade!")
# elif MARKS >= 80 and MARKS < 90:
#     print("You got a B grade!")
# elif MARKS >= 70 and MARKS < 80:
#     print("You got a C grade!") 
# elif MARKS >= 60 and MARKS < 70:
#     print("You got a D grade!")
# else:
#     print("You got an F grade!")

age = int(input("Enter your age: "))

if not (age >= 18):
    print("You are under 18")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")   
    