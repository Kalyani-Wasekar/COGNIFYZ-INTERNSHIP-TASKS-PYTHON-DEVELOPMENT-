def is_Palindrome(string):
    #Do the operation based on user input 
  if(string==string[::-1]):
      return"The string is a palindrome."  
  else:
      return "The string is not a palindrome." 
 
#Get the input from the user
string = input ("Enter a string you want: ") 
#display the message 
print(is_Palindrome(string))