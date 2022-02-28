/*
abba   aa
abab    abab
aabb    Empty String
aaabb  a
*/
string = input()
new_str = ""
j=0
while(len(string)!=0 or flag):
   if(string[i]!=string[i+1]):
       new_str += f"{string[i]}"
       string = string[:]
   j+=1
   if(j==5):
       flag=False
print(new_str)


 https://www.codechef.com/ide


[2,3,2,4,5,6,6,7,2,3]


Subset=6

Out: [2,2,2,[3,3]]
'''https://www.codechef.com/ide
 
 
[2,3,2,4,5,6,6,7,2,3]
 
 
Subset=6
 
Out: [2,2,2,[3,3]]
'''
list_subset = []
subset = []
n = 6
list_num = [2,3,2,4,5,6,6,7,2,3]
while(i<len(list_num)-1):
  

