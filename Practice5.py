from random import randint
listrand = []
a = randint (0,1)
n = 10
count = 0
count1 = 0
cnt = 0
cnt1 = 0
for i in range(n):
        listrand.append(randint(0,a))
print(listrand)
for i in range(len(listrand)):
    if listrand[i] == 1:
        count += 1
    else:
        count1 += 1
        print('Count 1 = ', count,' Count 0 = ', count1)
print('Вероятность 1 = ', count/len(listrand))
print('Вероятность 0 =', count1/len(listrand))
for j in range(len(listrand)-1):
    if (listrand[j] == 0) and (listrand[j+1] == listrand[j]):
        cnt += 1
    if (listrand[j] == 1) and (listrand[j+1] == listrand[j]):
        cnt1 += 1
