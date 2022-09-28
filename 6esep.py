#Сапи Аяжан
#лаборатория3
# генерирование 5 случайных целых чисел в диапазоне [0, 9]
import random
print('Function random.randrange(10)')
i=0
while i<5:
    d = random.randrange(10) # random.randrange(9+1)
    print(d)
    i = i+1
print