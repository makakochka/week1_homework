row = int(input("行数を入力してください: "))
column = int(input("行数を入力してください: "))

for i in range(1, row+1):
    for j in range(1, column+1):
        print(i*j, end=" ")
    print()
