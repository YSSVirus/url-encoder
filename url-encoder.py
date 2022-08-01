#!/usr/bin/python3

"""
Hey Judea! I hope you find this alot easier to read with all the notes and everything
I tried to make it as readable as I could I hope you enjoy
If your editor views these multi line comments weird try sublime'
I was wrong originally full encoding happens manually through the script while encoding of key characters on the other hand is handled by a package.
"""



#Here we import all of our needed libraries

from sys import stdout, argv
"""
stdout: We import this so we can print to standard output, this causes less issues when text doesnt want to display
argv: We import this so we can can take arguments from the user
""" 
from pathlib import Path # We import this so we can find the file path
import argparse # This is a super helpful argument parser, it helps simplify arguments and a  help menu along with a few other things.
import urllib.parse # This is what we use for encoding key characters

def aggressive_url_encode(string): # Here we pass our string variable to our url encode function
    return "".join("%{0:02x}".format(ord(char)) for char in string)
    """
    1. The ord function returns the Unicode code from a given character.
    2. Next we use the format function
    4. Next we use the join function with the hex declaration to join all or now hex text
    5. Next we look at the for loop, this tells us that it swaps out char with every character in the users string until it encodes everything
    6. The blank quotes in front make this combine with nothing seperating.
    Final: This command takes the users input, and seperates each letter, then encodes to unicode, then encodes it in hex, then we join all our now hex encoded characters with no seperator
    """

parser = argparse.ArgumentParser(usage='python3 url-encoder.py -ac -L list.txt', description='This script is made for url encoding either key characters or all characters.')
#here we crate the parser argument, we add in usage and description so users have a better understanding of the script
encoding_parser = argparse.ArgumentParser() # This is a small seperation this is our encoding parser, this is seperated as i had to make seperate rules
encoding = parser.add_mutually_exclusive_group(required=True) #This makes one of the the options mandetory
parser.add_argument('-l','-L','--l','--L', default='unencoded.txt', required=True, help='This is for defining the list of strings to encode') 
# This is the argument that holds the text to convert file its required as we need text to convert dont we?
encoding.add_argument('-kc','-KC','-kC','-Kc','--kc','--KC','--kC','--Kc', action='store_false', help='Use any of these to url encoding only KEY characters.')
#This is the argument that encodes key characters, I set it to store_false so we can make this decision between the two an easy boolean (true/false) question
encoding.add_argument('-ac','-AC','-aC','-Ac','--ac','--AC','--AC','--Ac', action='store_true', help='Use any of these to url encoding ALL characters')
#This is the argument that encodes all characters, I set it to store_true so we can make this decision between the two an easy boolean (true/false) question
encoding_args = encoding_parser.parse_args([]) #Here we made it a simple call to a variable to parse arguments

args = parser.parse_args() #Here we made it a simple call to a variable to parse arguments
file = Path(args.l) #get the path from the file args.l is how we call the -l argument

if file.exists(): # if then statement if it exists or if it does not
	with open (file) as f: # open the text file lets call it f
		for line in f: #call file line by line if were using the line lets call it line

			if args.ac == True: # this will be set to True if the user has the -ac argument. This is due to the action we set
				url_encoded = aggressive_url_encode(line) # here we call our aggressive url encoding function and set the output to the variable url_encoded
				stdout.write('The input: ' + line + ' has been change to ' + url_encoded) # This prints the encoded output in a nicee neat readable format 
			elif args.kc == False:# this will be set to False if the user has the -ac argument. This is due to the action we set
				url_encoded = urllib.parse.quote_plus(line) # Here we use urllib.parse to use "url quote plus" encoding
				stdout.write('The input ' + line + ' has been change to \n' + url_encoded) # This prints the encoded output in a nicee neat readable format 
			else: # area of -kc -ac arguments erroring out
				print("There was an error with checking how you want this converted. Keep in mind there is no input to these arguments, to -ac or -kc")
				# This is an error for if there -ac or -kc argument was messed up

else: # area of if then statement erroring out
	print('File is not real please try again') # Twlling the user to pick a real file as our check detected it wasnt real
