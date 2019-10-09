#Write a program that will ask the user to enter the amoutn of a purchase.
#The program should then compute the state and country sales tax. Assume the
#state sales tax is 5% and the country sales tax is 2.5%. The program
#should display the amount of the pruchase, the state sales tax, the county
#sales tax, the total sales tax, and the total of the sale (which is the sum
#of the amount of purchase plus the total sales tax).

price=float(input("Please enter the price: "))
state_tax=price*(5/100)
county_tax=price*(2.5/100)
subtotal=price+state_tax+county_tax

print("\nPrice= $"+format(price,',.2f'),"State tax= $"+format(state_tax,',.2f'),\
    "County tax= $"+format(county_tax,',.2f'),"Final price including tax= $"+format(subtotal,',.2f'),sep='\n')