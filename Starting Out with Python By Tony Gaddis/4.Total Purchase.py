#A customer in a store is purchasing five items. Write a program
#that asks for the price of each item, and then displays the subtotal
#of the sale, the amount  of sales tax, and the total. Assume the
#sales tax is 7 percent.

a=('first','second','third','fourth','fifth')
prices=[]
j=0
subtotal=0
for i in a:
    prices.append(float(input("Please enter the price of the "+i+" item: ")))
    subtotal=subtotal+prices[j]
    j+=1

sales_tax=subtotal*(7/100)
final_total_price=subtotal+sales_tax


print('\n'"Subtotal= $"+format(subtotal,',.2f'),"Sales tax= $"+format(sales_tax,",.2f"),"Final total price= $"\
                                                            +format(final_total_price,',.2f'),sep='\n')