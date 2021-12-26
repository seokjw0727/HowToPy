for x in "banana":    # for 구문을 사용하여 바나나를 출력하기
    print(x)



first = "Hello, World!"    # length를 사용하여 문자의 길이를 구할 수 있음
print(len(first))



test = "The best thigns in life are free!"    # in 을 사용하여 변수내부의 내용의 존재 여부를 확인 할 수 있음
print("free" in test)


# 다음과 같이 사용할 수 있다.
if "free" in test:
    print("변수 내부에 'Free'가 존재합니다.")
else:
    print("변수 내부에 'free'가 존재하지 않습니다.")

# 아래 코드와 상단의 else에 종속된 표현은 같은 효력이 있다.

if "things" not in test:
    print("변수 내부에 'things'가 존재하지 않습니다.")



