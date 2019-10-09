#Write a program that calculates the amount of money a person would earn
#over a period of time if his or her salary is one penny the first day,
#two pennies the second day, and continues to double each day. The program
#should ask the user for the number of days. Display a table showing what
#the salary was for each day,and then show the total pay at the end of the period.
#the output should be displayed ina dollar amount, nor the number of pennies.

number_of_days=int(input("How many days will you work? "))
daily_salary=.01
total_salary=0
print("\nNumber of Day\t\tSalary\n=============\t\t=====",)
for i in range(number_of_days):
    print("\t",i+1,"\t\t\t\t",'$'+str(daily_salary))
    total_salary=total_salary+daily_salary
    daily_salary=daily_salary*2

print("\nTotal pay after",number_of_days,"days is $ ",format(total_salary,',.2f'))