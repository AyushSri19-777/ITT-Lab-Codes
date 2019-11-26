import re

searchString = "Testing pattern matches"

expression1 = re.compile( r"Test" )
expression2 = re.compile( r"^Test" )
expression3 = re.compile( r"Test$" )
expression4 = re.compile( r"\b\w*es\b" )
expression5 = re.compile( r"t[^aeiou]", re.I )

if expression1.search( searchString ):
    print ('"Test" was found."')

if expression2.match( searchString ):
    print ('"Test" was found at the beginning of the line.')

if expression3.match( searchString ):
    print ('"Test" was found at the end of the line.')

result = expression4.findall( searchString )
print(result)
if result:
    print ('There are %d words(s) ending in "es":' % \
    ( len( result )) ),

    for item in result:
        print (" " + item)

print
result = expression5.findall( searchString )

if result:
    print ('The letter t, followed by a vowel, occurs %d times:'% \
    ( len( result ) )),

    for item in result:
        print (" " + item)
str="Hello ayush the time is 08:45 so goto sleep"
x=re.match("[0-9][0-9]",str)
print(x);
