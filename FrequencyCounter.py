# -*- coding: utf-8 -*-
#This program is meant to check the frequency of characters in a file(1st command line argument)


import sys
from collections import Counter


def main():
    
    try:
        file = open(sys.argv[1], 'r', encoding = "utf-8");
        frequencycount = Counter()
        for line in file:
            frequencycount+=Counter(line)
        print(frequencycount)
        file.close();
        
    except IOError:
        print ("The file passed as argument could not be found.")

    
    

    
main();