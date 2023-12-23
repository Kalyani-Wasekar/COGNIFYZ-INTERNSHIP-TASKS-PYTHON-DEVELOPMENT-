print("TEMPERATURE UNIT CONVERTER")
#Get the input from user
temp = float(input("Enter the temperature value you want="))
unit = input("Enter the unit of measurement (c for Celsius, f for Fahrenheit): ")
#Perform the conversion operation based on user input
if (unit == "c"):
        converted_temp = (temp * 9/5) + 32
        original_unit, target_unit = "Celsius", "Fahrenheit"
elif (unit == "f"):
        converted_temp = (temp - 32) * 5/9
        original_unit, target_unit = "Fahrenheit", "Celsius"
else:
        print("Invalid unit. Please enter 'c' or 'f'.")
#Display the derired temperature        
print(f"{temp} {original_unit} is equal to {converted_temp:.2f}{target_unit}.")




