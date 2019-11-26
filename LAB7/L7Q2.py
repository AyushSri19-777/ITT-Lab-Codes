print("\t\tTo remove punctuations from the string\n")
import string
str = input("Enter the string with punctuations:\n")
for i in string.punctuation:
    str = str.replace(i,"")
print("String after removing all the punctuations :\t",str)
