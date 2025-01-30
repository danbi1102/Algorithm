S = int(input())
sum = 0

for n in range(1, S+1):
    sum += n

    if sum == S:
        print(n)
        break

    elif sum > S:
        print(n-1)
        break
