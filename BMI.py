#!/usr/bin/env python
name = input('please enter your name:')
print(f"Hi {name.title()}! Let's calculate your BMI")
Height=float(input("Please enter your height in centimeters: "))
Weight=float(input("Please enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severely underweight")
	elif(BMI<=18.5):
		print("You are underweight")
	elif(BMI<=25):
		print("Great! You are Healthy.  Keep up the good habits")
	elif(BMI<=30):
		print("You are overweight")
	else: print("You are severely overweight")
else:("enter valid details")