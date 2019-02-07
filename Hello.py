'''
Created on Jan 10, 2019

@author: sthapa
'''
#print("hello World");

"""def my_function():
    print("test data");
    
my_function();"""

#============================
"""
x = lambda a : a + 10
print(x(5));
    
    
cars = ["car","bike","dozers"];
#rint(len(cars));

for x in cars:
    print(x);
"""

import os 
import datetime



def print_msg():
    print("\nContents from the logfile:");
    
         
         
working_dir = 'Edwisor';
file_name='2019.log';
my_path = os.path.join('C:\Analytics',working_dir)
my_file = os.path.join('C:\Analytics',working_dir,file_name)
my_files = os.listdir(my_path)
print("\n\n");

for filename in my_files:
    print(filename)
#open file in read-only mode and print it using the readlines()  
message_file = open(my_file, 'r')
print("\n\nContents from message file: {}".format(message_file.readline()))
input("Press Enter to continue....")
message_file.close()

message_file = open(my_file, 'a')
message_file.write("\n files backep up:" + str(datetime.datetime.now().strframe("%Y-%m-%d %H:%M")))
message_file.close()

message_file = open(my_file, 'r')
messages = message_file.readlines()


message_file.close()
print_msg(messages)


input("\n press Enter to exit... ")











    
    
    
    
    
    

    
    


    
    
    
