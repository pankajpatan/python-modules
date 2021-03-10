# Problem1 : write a Python program to read data from a file which has text containing emails,
#  write only the emails from the file into another file. 
#  You can use 're' module to extract emails from the text file.

# Problem 2:  Write a Python program to create a deque and 
# do Queue operations on it based on FIFO approach.. 
# use 'time' module to time your python code.
#  Display the time taken to insert an item to deque and to remove an item.


# Solution 1
print( "This is solution 1 , please check newEmail.txt to see results")

import re

file=open("emails.txt" ,"r")
pattern = "[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
emails_in_txt=file.read()
emails = re.findall(pattern,emails_in_txt)
file.close()

file2=open("newEmail.txt","w")
for words in emails:
    words=str(words)+" \n"
    file2.write(words)   
file2.close()





# Solution2

print( "This is solution 2")

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

import time

d=Deque()

start_time= time.time()
print(start_time)
d.addRear(5)
end_time=time.time()
print(end_time)
print(" the time taken to insert an item is (in seconds):" , (start_time-end_time))



start2_time= time.time()
print(start2_time)
d.removeRear()
end2_time=time.time()
print(end2_time)
print(" the time taken to remove an item is (in seconds):" , (start2_time-end2_time))
