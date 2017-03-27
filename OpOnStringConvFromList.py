#!/usr/bin/python
import re
import sys
"""python script to combine all the digits appearing between any two characters in a list
   containing digits and characters to a single number and then calculate the sum of the numbers
   in the modified list e.g; the sum of the digits in the list a=[1,2,3,'a','b',3,2,1] will be
   1+2+3+3+2+1=12 and if the list a=[1,2,3,'a',1,2,3,4,'b',3,2,1] then the sum will be
   1+2+3+1234+3+2+1=1246"""

a=[1,"a",1,2,3,32,"a",3,"w","e","d","f",4,3,"f",5,7,9,"g",5,"c",7,9,"d",1,23,3]
#a=['c',1,2,"a",1,2,3,4,5,'b','c','d',12,23,'e',123,'a','b',12,121,'c']
#a=['c',1,2,"a",1,2,3,4,5,'b','c','d',12,23,'e',123,'a','b',12,121,1]
#a=[1,1,2,"a",1,2,3,4,5,'b','c','d',12,23,'e',123,'a','b',12,121,1,'a']
#a=['c','a','b','d']
#a=[1,2,3,4]
print a + "\n"
#a =['a',3,'w','e','d','f',4,3,'f',5,'g',7,9]
if all(isinstance(item, str) for item in a):
        print "there are no integers in the list"
        sys.exit(0)
elif all(isinstance(item, int) for item in a):
        print sum(a)
else:
        a_to_string=''.join(str(i) for i in a)
        all_numbers=re.findall("\d+", a_to_string)
        if type(a[0])==int and type(a[-1])==int:
                all_numbers.pop(0)
                all_numbers.pop(len(all_numbers)-1)
                all_numbers_int=[int(i) for i in all_numbers]
                first_set=[]
                for item in a:
                        if type(item)!=int:
                                break
                        else:
                                first_set.append(item)
                second_set=[]
                for item in a[::-1]:
                        if type(item)!=int:
                                break
                        else:
                                second_set.append(item)
                print sum(all_numbers_int) + sum(first_set) + sum(second_set)
        elif type(a[0])!=int and type(a[-1])==int:
                all_numbers.pop(len(all_numbers)-1)
                all_numbers_int=[int(i) for i in all_numbers]
                second_set=[]
                for item in a[::-1]:
                        if type(item)!=int:
                                break
                        else:
                                second_set.append(item)

                print sum(all_numbers_int) + sum(second_set)
        elif type(a[0])==int and type(a[-1])!=int:
                all_numbers.pop(0)
                all_numbers_int=[int(i) for i in all_numbers]
                first_set=[]
                for item in a:
                        if type(item)!=int:
                                break
                        else:
                                first_set.append(item)

                print sum(all_numbers_int) + sum(first_set)
        else:
                all_numbers_int=[int(i) for i in all_numbers]
                print sum(all_numbers_int)