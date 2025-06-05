justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

answer =len(justice_league)
print("Number of Members",answer)
print(justice_league)
# Batman recruited Batgirl and Nightwing as new members.Add them to your list.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)
# Wonder Woman is now the leader of the Justice League Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print(justice_league)

# Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman"and move them in between Aquaman and Flash.
i=justice_league.index("Green Lantern")
j=justice_league.index("Aquaman")
justice_league[i],justice_league[j]=justice_league[j],justice_league[i]
print(justice_league)

# The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the followingnew members: "Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow".
justice_league.extend(["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"])
print(justice_league)
# Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print(justice_league)