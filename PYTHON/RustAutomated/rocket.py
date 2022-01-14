#   1 rocket        =       150 GP  +   10 explosives
#   10 explosives   =       500 GP  +   100 SULFUR      +   100 FRAGS   +   30 LOWGRADE

#   1 rocket    =   650 GP          +   100 SULFUR      +   100 FRAGS   +   30 LOWGRADE
#   650 GP      =       1300 SULFUR


#per 1400 sulf 100 stays sulf

totalSulfInK = 40



totalSulf = totalSulfInK * 1000

amtOfRockets = totalSulf / 1400
sulfNotGp = (totalSulf / 1400) * 100
gp = (totalSulf / 1400) * 650
sulfForGp = gp * 2
LGF = amtOfRockets * 30
frags = amtOfRockets * 100




print("total amt of sulfur: ",totalSulf)
print("rockets: ",amtOfRockets)
print("pure sulfur for rockets: ",sulfNotGp)
print("gp for rockets: ",gp)
print("sulfur for the gp: ",sulfForGp)
print("LGF for rocket: ",LGF)
print("frags for rockets: ",frags)
x = 30000+5106+5106+5106+1417+38+526+42+514+51
print(x)
y = 24175 + 4000
print(x-y)