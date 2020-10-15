#Assignment-2 and 3:
#Assignment-2

sample_string1="w3resource"
sample_string2 = "W3"
sample_string3 = "W"

str1=len(sample_string1)
str2=len(sample_string2)
str3=len(sample_string3)
#print(str)

array = []
for element in sample_string1:
    array.append(element)

#print(array)

nam1=array[0]
nam2=array[1]
nam3=array[len(array)-2]
nam4=array[len(array)-1]

c=nam1+nam2+nam3+nam4
print(c)

sample_string = "w3"

arr1 = []
for element in sample_string:
     arr1.append(element)
#print(arr1)
A=arr1[0]
B=arr1[1]
print(A+B+A+B)

if str1<2:
    print("Empty String-1")
elif str2<2:
    print("Empty String-0")
elif str3<2:
    print("Empty String")
else:
    print("Return")

#Assignment-3:
string ="restart"
char=string[0]
charcter={"r"}
#n=1
str1=string.replace(char,"$")
#str2=char+str1



print(str1)







