# # print("Hello World!")



# # print("""강한친구 대한육군
# # 강한친구 대한육군 """)




# # print("\    /\\")
# # print(" )  ( ')")
# # print("(  /  )")
# # print(" \(__)|")

# # # 배운점 : print 에서는 역슬래쉬를 두개를 써줘야 인식을 하더라



# # print("|\_/|")
# # print("|q p|   /}")
# # print('( 0 )"""\\')
# # print('|"^"`    |')
# # print('||_/=\\\__|')

# # # 배운점 : print 에서는 역슬래쉬를 두개를 출력 할 때, \\\ 이런식으로 3개를 써주어야 2개의 역슬래쉬를 출력한다.
# # # 그리고, print('') 이런식으로 작은 따옴표를 사용하는 습관을 가지도록 하자. 아니면, print 내부의 "" 과 싸우게 될 것이다.

# # A, B = input().split()   # 입력되는 문자를 input 함수로 입력받고, split 함수로 나누어 A, B 변수에 저장한다.
# # print(int(A)+int (B))    # int 함수로 A와 B를 정수로 변환 하고 두 수의 합을 출력함.



# # A, B = input().split()
# # print(int(A)+int (B))
# # print(int(A)-int (B))
# # print(int(A)*int (B))
# # print(int(A)//int (B))
# # print(int(A)%int (B))



# # A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
# # B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# # # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# # AxB2 = A * int(B[2])
# # AxB1 = A * int(B[1])
# # AxB0 = A * int(B[0])
# # AxB = A * int(B)

# # print(AxB2, AxB1, AxB0, AxB, sep='\n')
# # # sep='\n'로 줄바꿈



# # A,B = map(int,input().split())    # input 을 두개를 받는다.

# # if A > B:         # 해당 조건이 if 문
# #     print('>')
# # elif A < B:       # 위의 if 문이 거짓이 아니면, 해당 if문을 동작시킨다.
# #     print('<')
# # else:             # 둘다 거짓이라면, 해당 명령어를 실행한다.
# #     print('==')



# # score = int(input())    


# # if score >= 90:       # 만약, score 변수가 90점보다 크다면, A 출력
# #     print('A')
# # elif score >= 80:     # 만약, score 변수가 80점보다 크다면, B 출력
# #     print('B')
# # elif score >= 70:     # 만약, score 변수가 70점보다 크다면, C 출력
# #     print('C')
# # elif score >= 60:     # 만약, score 변수가 60점보다 크다면, D 출력
# #     print('D')
# # else:                 # 위의 상황이 아무것도 아니라면, F 출력
# #     print('F')






# duseh = int(input())
# if (duseh % 4 == 0 and duseh % 100 !=0) or duseh % 400 == 0:    # 만약 duseh 라는 변수가 4로 나눴을 때, 나머지가 0 이면서, 100으로 나눴을 때, 변수가 0 이거나, 400으로 나눴을 때, 나머지가 0이라면,
#     print('1')     # 1을 출력하고
# else:              # 조건이 거짓이라면, 
#     print('0')     # 0을 출력한다.



# pos_x = int(input())

# pos_y = int(input())

# if (pos_x >= 0 and pos_y >= 0):
#     print('1')
# if (pos_x <= 0 and pos_y <= 0):
#     print('3')
# if (pos_x <= 0 and pos_y >= 0):
#     print('2')
# if (pos_x >= 0 and pos_y <= 0): 
#     print('4')


# H, M = map(int, input().split())

# if M < 45 :	
#     if H == 0 :	
#         H = 23
#         M += 60
#     else :	
#         H -= 1	
#         M += 60
        
# print(H, M-45)	



# N = int(input())

# for i in range(1, 10):           # i 를 사용하여, 반복 가능한 요소를 하나씩 사용하며, 변수에 선언함.
#     print(N, '*', i, '=', N*i)   # 흔한 print



# T = int(input())        # T 라는 변수를 정수로 형태로 받는다.

# for _ in range(T):     # 
#     A,B = map(int, input().split())
#     print(A+B)



# print(input() + '??!')    # print의 매개변수에 입력을 받고, ??! 이라는 문자열을 더하여 출력한다.



# y = int(input())    # y를 정수형태로 입력받음

# print(y - 543);     # y에 543을 뺀 값을 출력함.


 
# n, m = map(int, input().split())

# print(n//m)     # n 을 m으로 나눈다.
# print(n%m)      # n 을 m으로 나눈 나머지를 구한다.


# A = int(input())
# B = int(input())

# print(A + B)
# print(A - B)
# print(A * B)



# a,b = map(int, input().split())
# print(a*(b-1)+1)    # 평균값에 1을 빼고, a를 곱해서 다시 1을 더하여 표현한다.




# A = int(input())
# B = int(input())

# print(A + B)


# print('.  .   .')
# print('|  | _ | _. _ ._ _  _')
# print('|/\|(/.|(_.(_)[ | )(/.')




# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# print(a + b + c + d + e)


# A, B = map(int, input().split());print(A + B)    # 처음으로 시작하는 극한의 최적화 코딩


# A = int(input()); print(A * 4);

# print('29\n'); print('seokjw0727');




# r1, s = map(int, input().split())

# print(2*s-r1)



# import sys

# ab12 = int(input())
# for i in range(ab12):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A + B)


# count = int(input())

# for i in range(count):     # i를 count 변수만큼 반복함. i의 기본값은 0
#     print(i+1)



# count = int(input())       # 위의 문제의 반대로 출력하는 코드이다.

# for i in range(count):
#     print(count-i)



# count = int(input())

# for i in range(count):
#     A, B = map(int, input().split())
#     result = (A + B)
#     print(f'Case #{i+1}: {result}')



# count = int(input())

# for i in range(count):
#     A, B = map(int, input().split())
#     result = (A + B)
#     print(f'Case #{i+1}: {A} + {B} = {result}')


# stars = int(input())

# for i in range(1, (stars+1)):
#     print('*' * i)  



# stars = int(input())

# for i in range(1, (stars+1)):
#     print(' ' * (stars - i ) + '*' * i)  


# A, B = map(int, input().split()); print(A + B)

# A, B, C = map(int, input().split()); print(A + B + C)


# print('고려대학교')

# A, B = map(int, input().split())

# print(A * B)

# N, K = map(int, input().split())
# A, B = map(int, input().split())

# print('비와이')


# N = int(input())

# print(int(N*0.78), int(N*0.8 + (N*0.2*0.78)))



# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# for i in range(N):
#     if A[i] < X:
#         print(A[i], end = ' ')



# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
    





# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break





# n = int(input())
# num = n
# count = 0

# while True:
#     a = num//10
#     b = num % 10
#     c = (a + b) % 10
#     num = (b * 10) + c

#     count = count + 1 
#     if(num == n):
#         break

# print(count)


# a = int(input())
# b = list(map(int, input().split()))

# print('{} {}'.format(min(b), max(b)))

num_list = []
for i in range(9):
    num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)





