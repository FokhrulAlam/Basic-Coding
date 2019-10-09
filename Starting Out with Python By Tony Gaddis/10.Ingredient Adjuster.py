#A cookie recipe calls for the following ingredients:
#1.5 cups of sugar
#1 cup of butter
#2.75 cups of flour
#The recipe produces 48 cookies with this amount of the ingredients.
#Write a program that asks the user how many cookies he or she wants to make.
#and then displays the number of cups of each ingredient needed for the
#specified number of cookies.

number_of_cookies=int(input("How many cookies do you want, please? "))

cups_of_suger=(1.5/48)*number_of_cookies
cups_of_butter=(1/48)*number_of_cookies
cups_of_flour=(2.75/48)*number_of_cookies

print(format(cups_of_suger,'.2f')+" cups of sugar, "+format(cups_of_butter,'.2f')+" cups of butter,"\
      +format(cups_of_flour,'.2f')+" cups of flour"+" is needed to make "+str(number_of_cookies)+" cookies.")