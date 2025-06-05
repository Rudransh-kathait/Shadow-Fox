Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

x=input ("Enter a city name:")
if x in Australia:
    print(f"{x} is in Australia")
elif x in UAE:
    print(f"{x} is in UAE")
else:
    print(f"{x} is in India")