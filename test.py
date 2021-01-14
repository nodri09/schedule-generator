import random as rnd

someList = []
for i in range(10):
    randomNum = rnd.randint(0, 10)
    someList.append(randomNum)

for i in someList:
    print(i)
