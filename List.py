

from tracemalloc import stop


family = ['mother', 'uncle', 'grandmother', 'me']   # 대괄호를 통해서 list를 만들 수 있다.


print(len(family))    # len 을 통해서 list에 몇개의 원소가 있는지 알려줍니다.

print(type(family))    # type 을 통해서 'family' 라는 변수의 클래스가 list 라는 것을 알 수 있습니다.

print(family)     # print를 사용해서 list 를 출력하면, 문자열이 그대로 출력됩니다.

print(family[1])    # list[리스트 순서] 를 사용해서 리스트의 내용을 가져 올 수 있습니다.




if "mother" in family:   # if 를 사용하여, "mother" 이라는 텍스트가 family 라는 list 내부에 존재 여부를 확인 할 수 있습니다.
    print("우리 가족에게는 어머니가 존재하십니다.")  

for a in family:   # for 반복문을 통해서 family 라는 list 를 출력 할 수 있습니다.
    print(a)


    




