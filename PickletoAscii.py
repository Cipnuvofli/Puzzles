# -*- coding: utf-8 -*-
#This program is meant to convert a pickled list containing lists of 2 item tuples ("#", 32) is 32 #'s for example, into ASCII Art. 
#It takes one command line argument(The pickled list file)
import pickle, sys

def main():
        unpickledfile = pickle.load(open(sys.argv[1], "rb"))
        for i in range(0,len(unpickledfile)):#This loop is for the rows of the art
            asciiline = ""#this stores the characters until output time
            for j in range(0, len(unpickledfile[i])):#This loop adds the contents of the tuples into a line of ascii art
                asciiline+=unpickledfile[i][j][0]*unpickledfile[i][j][1]
            asciiline+="\n"
            print(asciiline)
            asciiline = ""
    
   
       
        

        
            



main();