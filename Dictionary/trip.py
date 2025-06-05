your_expenses = {"Hotel": 1200,"Food": 800,"Transportation": 500,"Attractions": 300,"Miscellaneous": 200}
partner_expenses = {"Hotel": 1000,"Food": 900,"Transportation": 600,"Attractions": 400,"Miscellaneous": 150}

sum1 = sum(your_expenses.values())
sum2 = sum(partner_expenses.values())
print(sum1)
print(sum2)

if(sum1>sum2):
    print("Your expense is more")
elif(sum1<sum2):
    print("Your partner expense is more")
else:
    print("Both expense is same")

maxdiff=0
maxvalue=""

for i in your_expenses:
    diff=(your_expenses[i]-partner_expenses[i])
    if(maxdiff < diff):
        maxdiff=diff
        maxvalue=i

print(f"The biggest spending difference is in '{maxvalue}' with a difference of {maxdiff}.")
