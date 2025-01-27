num1 = int(input())
num2 = int(input())

num1a = int(num1/100)  # 4
num1b = int((num1-(num1a*100))/10)  # 7
num1c = int(num1-(num1a*100+num1b*10))  # 2

num2a = int(num2/100)  # 3
num2b = int((num2-(num2a*100))/10)  # 8
num2c = int(num2-(num2a*100+num2b*10))  # 5

ans1 = int(num1*num2c)
ans2 = int(num1*num2b)
ans3 = int(num1*num2a)

print(ans1, ans2, ans3, sep="\n")
print(ans1+(10*ans2)+(100*ans3))
