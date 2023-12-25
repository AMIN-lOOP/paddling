#AMIN LOOP

import random

print("ROCK - PAPER - SCISSOR")
print(" ")


p1 = input("PL-1 move (R/P/S): ").upper()

p2 = random.choice(['R', 'P', 'S'])

print(f"PL-2 move: {p2}")

if p1 == p2:
    print("Two players tied")
elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
    print("p1 wins")
else:
    print("p2 wins")
