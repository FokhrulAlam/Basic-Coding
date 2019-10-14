#Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored
# in a list. Use a loop to calculate the total sales for the week and display the result.

def sales_per_day():
    whole_week=[]
    days_of_week=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

    for days in range(7):
        sale=float(input("Please enter the sale of "+days_of_week[days]+" : "))
        whole_week.append(sale)
    return whole_week

def total_sales(whole_week_sale):
    total_sale=0
    for sale in whole_week_sale:
        total_sale=total_sale+sale
    return total_sale

def main():
    whole_week_sale=sales_per_day()
    sale_of_the_week=total_sales(whole_week_sale)
    print("\nThe total sales of the week is $"+format(sale_of_the_week,',.2f'))

main()