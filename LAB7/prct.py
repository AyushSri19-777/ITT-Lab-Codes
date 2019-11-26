import os
a=[1,2,3,5,4]
b=[1,3,4,5,4,4,2,4]
c={1,5,3,4,6}
print(max(a),min(b),len(b),c,list(c))
a.append(c)
print(b.count(4))
print(u'Hello Py!!')
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y=re.search("en$",txt)

if (y):
  print("YES! We have a match!")
else:
  print("No match")

import re

#Split the string at every white-space character:

str = "The rain in Spain"
x = re.split("a", str)
print(x)
