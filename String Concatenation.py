a = 123
b = 321
c = (a+b)   # a와 b를 더하는 수식을 c라는 변수에 저장함.

print(c)


h = "Hello"
w = "World!"
hw = h + " " + w   # 이런식으로 string도 가능함.

print(hw)


age = 16
explain = "Hello, My name is SJW and my age is {}"

print(explain.format(age))   # 원래는 불가능한 integer와 text를 함께 사용 할 수 있다.

grade = 3
explain2 = "Hello, My name is SJW and my age is {} in {}rd grade."

print(explain2.format(age, grade))   # 이런식으로 겹쳐서 사용할 수 있음.


# ---------------------------------------------------------------


text = "안녕하세요.\"멍청한\" 매코입니다."   # "" 내용속에 ""를 다시 사용하려면 \"\"을 사용할 수 있다.
print(text)


