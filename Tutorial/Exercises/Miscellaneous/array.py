from array import *
arr_num=array('i',[5,9,-8,4,2,0])
arr_char=array('u',['d','c','i'])

arr_unknown=array('u',(a for a in arr_char))

arr_unkn_num=array(arr_num.typecode,(a**2 for a in arr_num))
for i in range(len(arr_unkn_num)):
    print(arr_unkn_num[i],'',end='')
print()
for j in arr_unknown:
    print(j)