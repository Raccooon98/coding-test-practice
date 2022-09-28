# 반복
# n = int(input())
# for x in range(n):
#     print(x+1)

# 팩토리얼
# n = int(input())
# fac = 1
# for x in range(n):
#     fac= fac*(x+1)
# print(fac)

# A+B 반복수행
# n = int(input())
# for x in range(n):
#     a,b= map(int,input().split())
#     print(a+b)

#A+B 반복수행 탈출?

# while(True):
#     a,b = map(int,input().split())
#     if a==0 and b==0:
#         break
#     print(a+b)

#A+B 반복수행

# while(True):
#     try:
#         a,b = map(int,input().split())
#         print(a+b)
#     except:
#         break

# 구구단
# n =int(input())
# if 9>= n >=1:
#     for x in range(9):
#         print(f"{n} * {x+1} = {n*(x+1)}")

# 별찍기
num = int(input())
for x in range(num):
    for n in range(x+1):
        print("*",end='')
    print("")