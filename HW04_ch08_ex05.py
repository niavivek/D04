# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

#function to perform caesar cypher
def rotate_word(s,n):
    #initialize rotated word
    rot_string = ''
    val = 0 # value to store starting point
    for c in s:
        #if the letter is lower case, a is start point, else its A
        if c.islower():
            val = ord('a')
        else:
            val = ord('A')
            #substract the value of starting point and rotate
            # take modulus to go back to the same circle of alphabets
            #then add the value of starting point
            #basically bring the base to zero, and add the base back to get
            #the original character value - ASCII values
        rot_string += chr(((ord(c) + n - val) % 26) + val)
    return rot_string

def main():
    print(rotate_word("cheer",7))
    print(rotate_word("melon",-10))
    print(rotate_word("IBM",-1))

if __name__ == "__main__":
    main()