#Design a program that lets the user enter the total rainfall for each of 12 months into a list.The program should
# calculate and display the total rainfall for the year, the average monthlyrainfall, and the months with the
# highest and lowest amounts.

months=('January','February','March','April','May','June','July','August',\
            'September','October','November','December')
def rainfall_each_month():
    globals
    rainfall_list=[]
    for i in range(12):
        rainfall=float(input("Please enter the rainfall of "+months[i]+" : "))
        rainfall_list.append(rainfall)
    return rainfall_list

def calculate_rainfall(monthly_rainfall):
    total_rainfall=0
    for rainfall in monthly_rainfall:
        total_rainfall=total_rainfall+rainfall
    average_rainfall=total_rainfall/12
    print("\nTotal rainfall throughout the year is",total_rainfall)
    print("Average monthly rainfall is",average_rainfall,"\n")

def high_low_rainfall(monthly_rainfall):
    globals
    maximum_rainfall=max(monthly_rainfall)
    minimum_rainfall=min(monthly_rainfall)

    if minimum_rainfall != maximum_rainfall:
        for i in months:
            if months.index(i)==monthly_rainfall.index(maximum_rainfall):
                print("The highest amount of rain fell in",i)
            elif months.index(i)==monthly_rainfall.index(minimum_rainfall):
                print("The lowest amount of rain fell in",i)

    elif minimum_rainfall==maximum_rainfall:
        print("\nThe amount of rainfall each month was the same.")

def main():
    monthly_rainfall=rainfall_each_month()
    calculate_rainfall(monthly_rainfall)
    high_low_rainfall(monthly_rainfall)

main()