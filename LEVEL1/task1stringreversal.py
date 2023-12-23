#Take the string function to reverse
def reversed_str(input_str):
    reversed_str = input_str[::-1]
    return reversed_str
#Get the input from the user
original_str = input("Enter a string you want=")
reversed_result = reversed_str(original_str)
#Display the reverse string
print("Original_Str:",original_str)
print("Reversed Str:",reversed_result)
