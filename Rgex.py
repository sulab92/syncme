'''
Created on Feb 6, 2019

@author: sthapa
'''


import os

import re 

str = "The rain in Spain falls"

#print(os.getcwd());
#text = "contact.txt"
#x = re.findall("ai", txt )
#x = re.search("\s", str)

#print("The first white-space character is located in position:", x.start())

#x = re.search("Portugal", str)
#x = re.split("\s", str)
#for first occurance

#x = re.split("\s", str, 1)

#sub function
#x = re.sub("\s", "9", str)

#x = re.search(r"\bS\w+", str)
#x = re.findall("\d", str) #to fetch all the number/digit fields
#x = re.findall("S...n" , str)

#x = re.findall("al{2}", str)
x = re.findall("rain|Spain", str)
print(x)
#print(x.span())




