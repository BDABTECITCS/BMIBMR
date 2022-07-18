Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #ver 3
import time
print("Welcome to the BMI BMR Calculator!")#welcomes the user
print("")
name = str(input("Please enter full name: "))

validInteger = False  #It sets the validInteger to False

while not validInteger:
    weight = input("Enter your weight(KG): ")  #User input for weight
    if weight.isdigit():  #If statement if user inputs valid integer
        validInteger = True  #It sets the validInteger to True
    else:  #Else statement if user doesnt input validinteger
        print("You must enter a valid weight, Please enter your weight in nunmbers.")


validInteger = False  #It sets the validInteger to False

while not validInteger:
    height = input("Enter your height(CM): ")  #User input for height
    if height.isdigit():
        validInteger = True  #It sets the validInteger to True
    else:  #Else statement if user doesnt input validinteger
        print("You must enter a valid height, Please enter your height in numbers.")  #


validInteger = False  #It sets the validInteger to False

while not validInteger:
    age = input("Enter your age: ") #User input for age
    if age.isdigit():  #If statement if user inputs valid integer
        validInteger = True  #It sets the validInteger to True
    else:  #Else statement if user doesnt input validinteger
        print("You must enter a valid age, Please enter your age in nunmbers.")

bmi = int(weight)/(int(height)/100)**2# the formula for BODY MASS INDEX
onedecbmi = format(bmi, ".1f")#onedecbmi is a variable which allows the BMI turn into be one decimal point, which allows the result to round up to one decimal point
print("Your BMI is", onedecbmi)#print out the users BMI
if bmi <= 18.5:#if statment, if the bmi is lower than 18.5 it print out underweight
  print("You are underweight.")
elif bmi <= 24.9:#elif statment is between 18.5 and 24.8 then its healthy 
  print("You are healthy.")
elif bmi <= 29.9:#elif statment, is between 24.9 and 29.8 then prints overweight
  print("You are overweight.")
elif bmi <= 34.9:#elif statment, is between 30 and 34.9 then prints serverley overweight
  print("You are severeley overweight.")
elif bmi <= 39.9:#elif statment, is the bmi is between 34.9 and 39.9 the the user is obese
  print("You are obese.")
else:#else statment, is anything is above 39.9 the the user serverely obese
  print("You are severeley obese.")  
print ("")

time.sleep(3)

validLetter = False

yesnobmr = str(input("Would you like to calculatge your BMR(Basal Metabolic Rate) (y)es or (n)o? :")) #asks the user if they would like to calculate their bmr
if yesnobmr == "y":#if statment, is the user says y then it calculates the bmr
  print("Wait a few seconds")
else:
  print("Thank you for using the BMI BMR app.")
  exit()

print("")
MaleOrFemale = str(input("Are you a (m)ale or a (f)emale? "))
print("Please wait a few seconds")#asks the user if they are male of female
time.sleep(2)#delays by 1 second

if MaleOrFemale == "m":#if statment, if the the user says m then it calculates the male 
  MaleOrFemale = "m"#variable local
  bmr = 88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * int(age))#formula for bmr male
  TwoDecimalPoints = format(bmr, ".2f")#making the bmr to 2 decimals points
  print("Your basal metabolic rate is " + format(bmr, ".2f"))#prints out the  bmr to two decimal points to the user

elif MaleOrFemale == "f":#elif statment, if the user says f then it calculates the female
  MaleOrFemale = "f"#local variable
  bmr = 447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * int(age))#formula for bmr female
  TwoDecimalPoints = format(bmr, ".2f")#rounds the decimal point to 2 decimals
  print("Your basal metabolic rate is " + format(bmr, ".2f"))#prints the bmr to the user
print("")
print("Now we are going to find out how much calories you need to maintain your current weight")#checks to see how much calories needs to maintain

def daily_calorie(bmr):#function for daily calorie
  print("1 = Do not exercise")#no exercise
  
  print("2 = Exercises 1 - 3 times per week")#exercises 1-2 times
  
  print("3 = Exercises 4 - 5 times per week")#exercises 4-5 times
  
  print("4 = Exersises intensely 2 - 5 times per week")#exercises intense 2-5
  
  print("5 = Exercises intensely 6 times a per week")#exercises intense 6
daily_calorie(bmr)#call function
print("")
activeness = False#user actice if false do this
while not activeness:#while loop
  try:#try statment will occur
    activeness = int(input("Select your activity level: "))#asks to select actice
    if activeness == "1":# if active 1 then continue
      activeness = True
    if activeness == "2":# if active 2 then continue
      activeness = True
    if activeness == "3":# if active 3 then continue
      activeness = True
    if activeness == "4":# if active 4 then continue
      activeness = True 
    if activeness == "5":# if active 5 then continue
      activeness = True
  except:#if its not a number then print
    print("invalid activity level, please enter a number from 1 to 5.")

if activeness == 1:
  activenessIndex  = 1.2 #index for the activeness
elif activeness == 2:
  activenessIndex = 1.375#index for the activeness
elif activeness == 3:
  activenessIndex = 1.46#index for the activeness
elif activeness == 4:
  activenessIndex = 1.725#index for the activeness
elif activeness == 5:
  activenessIndex = 1.9#index for the activeness
print("")
print("Please wait a few seconds.")
time.sleep(3)
print("")
daycalorieneed = int(bmr * activenessIndex)#how much daily calories
print("To maintain your current weight you need to keep eaing " + str(daycalorieneed) + " calories per day." ) 
print("")
def calculate_macro(calorie):#function for macros
  calorie_from_protien = int(.4 * calorie)#how many calories in protien
  calorie_in_protien = int(calorie_from_protien / 4)#how many calories in protien 
  calorie_from_carb = int(.4 * calorie)#how many calories in carbs
  calorie_in_carb = int(calorie_from_carb / 4)#how many calories in carbs 
  calorie_from_fat = int(.2 * calorie)#how many calories in fat 
  calorie_in_fat = int(calorie_from_fat / 9)#how many calories in fat
  print("These are the calories from Protien, Carb and fat intake")
  print("Caloires from Protien = " + str(calorie_from_protien) + " Therefore you will need " + str(calorie_in_protien) + " grams of protien." )
  print("")
  print("Caloires from Carbs = " + str(calorie_from_carb) + " Therefore you will need " + str(calorie_in_carb) + " grams of carbs." )
  print("")
  print("Caloires from fat = " + str(calorie_from_fat) + " Therefore you will need " + str(calorie_in_fat) + " grams of fat." )
  print("")
if bmi:
  calculate_macro(daycalorieneed)#call function

print("Thank you for using the BMI BMI app")
time.sleep(3)
f = open("peoplewhousedtheapp.txt" , "a")#creates a file
f.write("NAME: "+ "\n")#writes name of user \n goes to the next line
f.write(name + "\n")#writes name of user \n goes to the next line
f.write("WEIGHT OF THE USER: " + "\n")#writes weight of user \n goes to the next line
f.write(str(weight) + "KG" + "\n")#writes weight of user \n goes to the next line
f.write("HEIGHT OF THE USER: " + "\n")#writes height of user \n goes to the next line
f.write(str(height) + "CM" + "\n")#writes height of user \n goes to the next line
f.write("AGE:" + "\n")#writes age of user \n goes to the next line
f.write(str(age) +"\n")#writes age of user \n goes to the next line
f.write("BODY MASS INDEX: " + "\n")#writes bmi of user \n goes to the next line
f.write(str(onedecbmi) + "\n")#writes bmi of user \n goes to the next line
f.write("Your target BODY MASS INDEX is between 20 - 24 " + "\n")#writes target of user \n goes to the next line
f.write("BASAL METABOLIC RATE: " + "\n" + "\n")#writes bmr of user \n goes to the next line
f.write(str(TwoDecimalPoints) + "\n" + "\n")#writes bmr of user \n goes to the next line

f.close()#closes the file

f = open("peoplewhousedtheapp.txt", "r")  #open the file
print(f.read())#prints out the file created
