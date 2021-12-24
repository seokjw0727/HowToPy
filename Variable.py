# 변수에 관련한 코드! 










# 자기소개를 해주세요. 

print("나는 멍청합니다.") # 가장 기본적으로 표현할 수 있음

""" 그러나 나의 상태가 변경된다면?
변수를 활용하는 것이 편안하다 """

# 변수들

name = "석지우" # 숫자가 아니기 때문에 ""을 사용해야 함.

age = 16

state = "멍청"


print("나의 이름은" + str(name) + "입니다. 그리고, 나이는" + str(age) + "입니다. 마지막으로, 저는" + str(state) + "합니다.")
# 해당처럼 변수를 사용할 수 있음


# 또는 Boolean과 함께 변수를 사용할 수 있음.


def gender(gender) :
    if gender >= 1:
        gender = "남성"
        print (gender)
    else:
        gender = "여성"
        print (gender)


gender(gender=0)
