def users(names):
    number=0
    for i in names:
        count_char = 0
        for cha_r in i:
            count_char += 1
            if count_char > 5:
                number += 1
    return number

print("Please enter ten names below:")
name=[]

for i in range(10):
    n=input()
    name.append(n)

number=users(name)
print("Number of names having more than five characters is ",number)