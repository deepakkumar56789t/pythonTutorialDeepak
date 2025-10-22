import pandas as pd
import numpy as np


ser = pd.Series()
print("Pandas Series: ", ser)

data = np.array(['g', 'e', 'e', 'k', 's'])

ser = pd.Series(data)
print("Pandas Series:\n", ser)


print("----------after pandas ---------------")
str="Deepak!!!!!!"
str2="this is a string"
str3="this is a string"
print(str.rstrip("!"))  # ! can be stripe out
print(str2.capitalize())   # String convert into the camelcase character

print(str3.count("t")) #count the character of t

print(str2.find("is")) #find the index of given character
print(str2.index("is"))  #check string contains digit occurs at which index

print(str2.isupper())  #check string is in lower case or not
print(str2.islower())  #check string is in lower case or not

print(str2.isdigit()) #check string in digit or not
print(str2.isalpha()) #check string contains alpha character of not
print(str2.isalnum())  #check string contains alpha  umeric or not
print(str2.isspace()) #check string contains spaces
print(str2.isnumeric())  #check string is numeric or not

print(str2.upper())  #convert string to upper
print(str2.lower())  #convert string to lower





