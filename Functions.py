# 드디어 함수를 배우는구나...


def my_funciton():   # def 함수이름(파라미터):    형태를 통해서 함수를 선언할 수 있다.
    print("Hello from a funciton")


my_funciton()    # 함수이름(파라미터) 형태를 통해서 함수를 호출 할 수 있다.



def 잘생긴(name):     # 파라미터가 포함된 함수
    print("엄청 잘생긴" + name)



잘생긴(             # 파라미터에 값을 집어넣는 방법
    name="매코"
)


def ex(*kids):     # 파라미터를 list 처럼 정의 할 수 있으며, 불러올 수 있다.
    print("가장 멋있는 것은 " + kids[2])

ex("동해물", "백두산", "남산", "소나무")



def func(name1, name2, name3):    # 여러개의 파라미터를 선언 할 수 있다.
    print("여러분들의 이름은 " + name1 + name2 + name3 + " 입니다.")

func(    # 여러개의 파라미터 지정하기
    name1="매코",    # 이건 나임 ㅎ
    name2="메빵",    # 친구 별명임 
    name3="송사리"   # 나 싫어하는 사람 별명임 ㅠ
)




# if 와 함수를 통해서 수학적인 계산을 할 수 있다.

def math(a, b, c):
    if(a > 0):
        print("a는 양수입니다.")
    else:
        print("a는 음수입니다.")
    if(b > 0):
        print("b는 양수입니다.")
    else:
        print("b는 음수입니다.")
    if(c > 0):
        print("c는 양수입니다.")
    else:
        print("c는 음수입니다.")


math(
    a=5,
    b=7,
    c=-123897
)