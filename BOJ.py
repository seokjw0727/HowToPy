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


H, M = map(int, input().split())

if M < 45 :	
    if H == 0 :	
        H = 23
        M += 60
    else :	
        H -= 1	
        M += 60
        
print(H, M-45)	