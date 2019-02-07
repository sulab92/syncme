'''
Created on Feb 4, 2019

@author: sthapa
'''


import os


#print(os.getcwd());
working_dir = 'Edwisor';
file_name='contact.txt';
my_path = os.path.join('C:\Analytics',working_dir)
my_file = os.path.join('C:\Analytics',working_dir,file_name)
my_files = os.listdir(my_path)

for filename in my_files:
    print(filename)
#open file in read-only mode and print it using the readlines()  
message_file = open(my_file, 'r')
print("\n\nContents from message file: {}".format(message_file.readline()))

#message_file.close()
def isPhoneNumber(file_name):
    if len(file_name) != 12:
        return False
    for i in range(0,3):
        if not file_name[i].isdecimal():
            return False
    if file_name[3] != '-':
        return False
    for i in range(4, 7):
      if not file_name[i].isdecimal():
        return False
    if file_name[7] != '-':
        return False
    for i in range(8, 12):
        if not file_name[i].isdecimal():
             return False
    return True
            
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))            
        
         
          
          
            
        
           
          
        
