Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

x=input("Enter your first city")
y=input("Enter your second city")

if x and y in India :
    print("Both cities are in India")
elif x and y in UAE :
    print("Both cities are in UAE")
elif x and y in Australia :
    print("Both cities are in Australia")
else:
    print("They don't belong to same country")