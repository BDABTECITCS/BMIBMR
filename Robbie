# BMIBMR
#BMI BMR v4
print("Welcome to the BMI BMR calculator. This program calculates your Body Mass Index and your Basal Metabolic Rate.")

username = input("Enter your username: ")

print()

heightval = False

while not heightval:
  try:
    height = float(input("Please enter height in cm from 1-300: "))
    if height >= 1 and height <= 300:
      heightval = True
  except:
    print("You must enter a valid height from 1 to 300.")
print("Your height is:",height)





weightval = False

while not weightval:
  try:
    weight = float(input("Please enter weight in kg from 1-500: "))
    if weight >= 1 and height <= 500:
      weightval = True
  except:
    print("You must enter a valid weight from 1 to 500.")
print("Your weight is:",weight)



  

ageval = False

while not ageval:
  try:
    age = float(input("Enter age from 1-126: "))
    if age >= 1 and age <= 126:
      ageval = True
  except:
    print("You must enter a valid age.")
print("Your age is:",age)





gender = input("Enter gender. Type 'male' or 'female': ")
if gender == "male":
  print("Your gender is:",gender)
elif gender == "female":
  print("Your gender is:",gender)
else:
  print("You must enter a valid gender.")
    




#BMI
def f_bmi():
  BMI = weight / (height/100)**2
  print(f"Your BMI is {round(BMI,2)}")
  if BMI <= 18.4:
    print("You're underweight")
  elif BMI <= 24.9:
    print("You are healthy weight")
  elif BMI <= 29.9:
    print("You are over weight")
  elif BMI <= 34.9:
    print("You are really over weight")
  elif BMI <= 39.9:
    print("You are obese")
  else:
    print("You are severely obese")

#BMR

def f_bmr():
  if gender == "male":
    print("Your BMR is",(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)),"Kcal/Day")

  if gender == "female":
    print("Your BMR is",(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)),"Kcal/Day")

print()

print("What would you like to measure?")
print("Option 1: BMI")
print("Option 2: BMR")

usinput = input("Please type '1' or '2' to choose an option. ")

print()

if usinput == "1":
  f_bmi()

elif usinput == "2":
  f_bmr()

else:
  print("Please enter one of the displayed options.")

print()

f = open("demofile.txt","w")
f.write(("Your data is: ") + "\n")
f.write("Your name is: " + username +"\n")
f.write("Your height is: " + str(height)+("cm")+"\n")
f.write("Your weight is: " + str(weight)+("kg")+"\n")
f.write("Your age is: "+str(age)+"\n")
f.write("Your BMI is: "+str(weight / (height/100)**2)+"\n")

f.close()

f=open("demofile.txt", "r")
print(f.read())
