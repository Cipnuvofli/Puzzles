# -*- coding: utf-8 -*-


#this program is meant to rotate the english text in a text file(first argument) after converting it to lower case
#the rotation amount is a value(second argument) and stored in result.txt
#for example, with argument of 2, the letter a would become the letter c, b to d, etc
#It should also include some level of checking for erroneous input
import sys, string

#On establishing the shift in the character variable.
#1. To Establish the shift, take the ascii value of the original character
# and then subtract the ascii value of a to put it on a 0 to 25 number scale where
# 0 is a and 25 is z

#2. then add the value of the shift to it

#3. Next, divide the result modulo 26 to account for characters
# like z and very large shifts. At this point the actual shift has been established

#4. Add the Ascii value of a to the shift to put it back on the Ascii letter spectrum 

def main():
    try:
        originalfile = open(sys.argv[1], 'r', encoding = "utf-8");
        result = open('result.txt', 'w', encoding = "utf-8");
        for line in originalfile:
            line = line.lower()
            translatedline = ""
            for character in line:
                if character in string.ascii_letters:
                    character = chr((ord(character)-ord('a')+int(sys.argv[2]))%26 + ord('a'))
                    translatedline+=character                                        
                else:
                    translatedline+=character
            result.write(translatedline)
        originalfile.close();
        result.close()
    except IOError:
        print ("The file passed as argument could not be found.")


        
        
main();
                   