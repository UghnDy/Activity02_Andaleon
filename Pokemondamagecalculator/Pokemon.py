import random

modifiers ={
    "Target": 0.5,
    "Weather": 1.5,
    "Badge": 1.25,
    "Critical": 2,
    "Random": random.uniform(0.85, 1),
    "Stab": 1.5,
    "Type":  random.uniform (0.25, 0.50),
    "burn": 1,
    "other": 1,
}

sumMod = 1      
for x in modifiers:
    sumMod *= modifiers[x]

level = 90
power = 110
a = 205
d = 188

damage = ((((((2 * level)/5) + 2) * power * (a/5))/50) +2) * float(sumMod)

print(damage)