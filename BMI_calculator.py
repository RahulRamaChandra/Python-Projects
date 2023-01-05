"""The Body Mass Index or BMI is calculated from weight and height of a Person.

What is Body Mass Index (BMI)?

BMI is a measure of relative weight based on an individual’s mass and height.
Today, Body Mass Index is commonly used to classify people as underweight, overweight, and even with obesity.
Also, it is adopted by countries to promote healthy eating.

BMI can be considered as an alternative for direct measurements of body fat.
Besides, BMI is an inexpensive and easy-to-perform method of screening for weight classes that may cause health problems.

BMI Calculator with Python

The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, then dividing the answer again by their height."""


Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height/100
BMI = Weight / (Height * Height)
print("your Body Mass Index is: ", BMI)
if(BMI>0):
    if(BMI<=16):
        print("you are severly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are Healthy")
    elif(BMI<30):
        print("you are overweight")
    else:print("you are severly overweight")
else:("enter valid details")