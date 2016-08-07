#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    #this is correct, it returns True if it finds a lower case character
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    #this is not checking if the string has lower case character but 
    #rather if the character 'c'
    #is lower case
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower() # flag is changed for every character - this means that if
        #the last character checked is upper case -it would return false even if
        #there are other lower case characters in the string
    return flag #if string is empty flag is not assigned any value and also not initialized
    #might throw error


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    #nothing wrong here
    flag = False # correct -flag is initialized
    for c in s:
        flag = flag or c.islower()#correct-maintains the True case even if there is and upper case later
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():#returns false even if any character is upper case
            return False
    return True # returns true even for empty string


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("thisstringmessesupthefunction"))
    print(any_lowercase2("thisstringmessesupthefunction"))
    print(any_lowercase3("thisstringmessesupthefunction"))
    print(any_lowercase4("thisstringmessesupthefunction"))
    print(any_lowercase5("thisstringmessesupthefunction"))


if __name__ == '__main__':
    main()
