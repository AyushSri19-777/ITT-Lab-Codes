print("\t\tTo print environmental variables\n")
import os
print("\n",os.environ,"\n\n")
str=input("Enter the directory:\n")
print(os.environ[str])
