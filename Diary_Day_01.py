""" Python Notes from Sn0wF0x """


print("Welcome to Sn0wF0x notes about Python :) \n")
print("=========================================\n")
print("Lets Begin with some Basic Variables\n")


""" 

Some Juicy Variables, we will use later on! 

"""
#This is a Simple Text String
BasicString="I am some Text in a String"
#This is a Simple int 
BasicInt=42
#This is a Simple Float
BasicFloat=3.14
#A Sample Word for Lauter usage!
word="Nightlife"



"""And this is me, printing them all out
#Btw if you might ask, the "\n" is for a break """
print("The Text is: ",BasicString,"\nThe Number is:",BasicInt,"\nThe Float is: ",BasicFloat)



""" Having Fun with Strings: 

Part 01 => Look for a Random Letter in A String 	"""
print("\nNow to Something interesting...\nThe following word can be counted in each character:NightLife\n")
print("The Third Letter of This word is... ")
print(word[3])
print("\nbut thats clearly the Fourth! Nah..\nnot really because array ALWAYS starts at 0\n")
print("That basicallyy means:\n")
print("Letter 0:",word[0],"\nLetter 1:",word[1],"\nLetter 2:",word[2],"\nLetter 3:",word[3],"\nLetter 4:",word[4],"..etc\n\n")


""" Having Fun with Strings: 

\b => backspace
\t => Tabulator
\n => New Line 

Part 02 => Lets try to use a Range of Characters of A String 	"""
print("And now Lets not only Take one, but several Characters!")
print(word[3:7],"\n")

""" Having Fun with Strings: 
Part 03 => And now... BACKWARDS!"""

print("And Now... Backwards: \n",word[::-1],"\n") 

""" Having Fun with Strings: 
Part 04 -> Splitting me Softly """

print("We now have a new string: Hello World!\n")
print("Lets see how it Looks like when We Split it!\n")

ExampleString='Hello World'
ExampleStrinSplitted=ExampleString.split()[1]
print("The Second Part of our String is: ",ExampleStrinSplitted," \n")
print("And now the Same but with a Seperator (e) :\n")
ExampleStrinSplittednew=ExampleString.split('e')[0]
print("The first Part of the String is: ",ExampleStrinSplittednew,"\n")