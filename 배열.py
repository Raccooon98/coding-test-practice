# x 보다 작은 수 출력
# n, x = map(int,input().split())
# A = list(map(int,input().split()))
# for i in range(n):
#     if A[i]<x:
#         print(A[i], end=" ")

# n = int(input())
# A= list(map(int,input().split()))
# v= int(input())
# print(A.count(v))
num = []
for i in range(30):
    num.append(i+1)
for n in range(28):
    num.remove(int(input()))
print(min(num))
print(max(num))