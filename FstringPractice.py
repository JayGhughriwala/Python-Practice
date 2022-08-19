print("This is a program of the practice of the F string ")



print("First of all a traditional way to insert a new string in to a another string ")
#this is a traditional way to insert a new string in to a another string but it is not good to use it because it is not efficient if string is too big
# str = "Hello World"

# str1= "Jay %s" % str
# print(str1)

#  Another way

# str1 = "Jay"
# str2= "Hello World"
#
# str3="Hello {} {}"
#
# str4=str3.format(str1,str2)
# print(str4)


# Now practice of the F string
import math
str1 = "Jay"
str2="Hello World"

str3= f"Hello {str1} {str2} {5*5} {math.sqrt(25)}"
print(str3)