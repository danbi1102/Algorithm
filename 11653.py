N = int(input())

while N > 1:
    for i in range(2, N+1):  # 그냥 N까지로 하면 N이 1이어서 소인수분해 결과 끝까지 출력 안 됨
        if N % i == 0:
            N = N//i
            print(i)
            break
