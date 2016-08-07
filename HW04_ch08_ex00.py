#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


# Body
def count(string,letter):
	count = 0
    #take each character and look for the letter
	for s in string:
		if s == letter:
			count += 1#count if found
	print ("Number of %s's in %s is %d" % (letter,string,count))


###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count("value","u")
    count("hello","l")
    count("This world is amazingly awesome","a")
    count("University of California Berkeley","e")


if __name__ == '__main__':
    main()
