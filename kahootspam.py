from kahoot import client
import random

bots=[]
print("How many bots? ")
botcount=int(input())
print("What PIN? ")
pin=int(input())
for i in range(botcount):
    bots+=[client()]
for i in bots:
    i.join(pin,str(random.choice(range(100000))))
