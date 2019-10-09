#Write a program that will ask the user to enter the amount of a purchase.
#The program should then compute the state and country sales tax. Assume the
#state sales tax is 5% and the country sales tax is 2.5%. The program
#should display the amount of the pruchase, the state sales tax, the county
#sales tax, the total sales tax, and the total of the sale (which is the sum
#of the amount of purchase plus the total sales tax).
#Write the whole program using functions.

def price():
    purchase_amount=float(input("Please enter the total amount of purchase: "))
    return purchase_amount
def state_tax(total_purchase):
    state_tax=total_purchase*(5/100)
    return state_tax
def county_tax(total_purchase):
    county_tax=total_purchase*(2.5/100)
    return county_tax
def subtotal(total_purchase,state_tax,county_tax):
    subtotal=total_purchase+state_tax+county_tax
    return subtotal
def output_printing(total_purchase,state_tax,county_tax,subtotal):
    print("\nPrice= $" + format(total_purchase, ',.2f'), "State tax= $" + format(state_tax, ',.2f'), \
          "County tax= $" + format(county_tax, ',.2f'), "Final price including tax= $" + format(subtotal, ',.2f'),
          sep='\n')
def main():
    purchase_amount=price()
    tax_by_state=state_tax(purchase_amount)
    tax_by_county=county_tax(purchase_amount)
    price_including_taxes=subtotal(purchase_amount,tax_by_state,tax_by_county)
    output_printing(purchase_amount,tax_by_state,tax_by_county,price_including_taxes)

main()


