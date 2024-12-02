import random

faces_num = int(input("サイコロの面の数は?: "))
roll_dice_num = int(input("何回振りますか?: "))

results = []
for i in range(roll_dice_num):
    results.append(random.randint(1, faces_num))

print(results)
