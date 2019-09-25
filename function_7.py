def our_function(numbers):
   even_number=0
   total_numbers=0
   for i in numbers:
       if i%2==0:
           even_number+=1
       total_numbers+=1
   odd_number=total_numbers-even_number

   return(even_number,odd_number)

num_list=[]
print("Please enter some integers:")
for i in range(0,10):
    lst=int(input())
    num_list.append(lst)

x,y=our_function(num_list)

print("Total even numbers: ",x)
print("Total odd numbers: ",y)